
from flask import Flask, jsonify, request
import json

import dill


### Importing librairies :

import numpy as np
import tensorflow as tf
import pickle

### Importing useful functions :

from tensorflow.keras.applications.resnet50 import preprocess_input 
# The images are converted from RGB to BGR, 
# then each color channel is zero-centered with respect to the ImageNet dataset, without scaling.

from keras.preprocessing import image


app = Flask(__name__)

# Load pre-trained models :
    
def load_model():
    model = tf.keras.models.load_model('ResNet50_pretrained_2.h5')
    return(model)
    
def load_dict_classes():
    with open('dict_classes.pkl', 'rb') as file:
        dict_classes = pickle.load(file)
    return(dict_classes)


    

#### Creation of the unique function :
@app.route('/predict_breed', methods=['GET'])
def predict_breed(image_path: str = ""):
    """Predict breed for a given image path.

    Args:
        image_path (str): input dog image path to predict breed for.
    """

    ### Definition of the input image :
    
    #image_input = input('Please enter the path of the image, without "" : ')
    #image_input = r"C:\Users\may81\Data Science Projects\OpenClassroom\Projet 6 - Classez des images avec des algorithmes de Deep Learning\Images\n02110185-Siberian_husky\n02110185_14650.jpg"
    
    # parse input features from request
    request_json = request.get_json()
    image_path = str(request_json["input"])
    
    image_array = image.img_to_array(image.load_img(image_path))
    
    ### Preprocessing :
        
    # Resizing to 224x224 :
        
    resized_image = tf.keras.preprocessing.image.smart_resize(image_array, size=(224,224))
    
    
    # Preprocessing with the keras preprocessor :
        
    preprocessed_image = preprocess_input(resized_image)
    
    
    # Expand image dimensions to match required size (as trained with mini-batches)
    
    preprocessed_image_expanded = np.expand_dims(preprocessed_image, axis=0)
    
    
    ### Making prediction :
        
    # Get outputs from predictions :
        
    from tensorflow import keras
    #model = keras.models.load_model(r"C:\Users\may81\Data Science Projects\OpenClassroom\Projet 6 - Classez des images avec des algorithmes de Deep Learning\Classez_des_images_a_l_aide_d_algorithmes_de_deep_learning_May_Morgan\ResNet50_pretrained_2.h5")
    
    model = load_model()
    
    predictions = model.predict(preprocessed_image_expanded)
     
    # Get the predicted breed using the class dictionary :
    
    class_index = np.argmax(predictions,axis=1)
    
    dict_classes = load_dict_classes()
    
    breed = list(dict_classes.keys())[list(dict_classes.values()).index(class_index)]
    
    ### Printing the result :
        
    response = json.dumps({'response': breed.split('-')[1].replace('_', ' ')})
    
    return response, 200
    


if __name__ == '__main__':
    app.run(debug=True)