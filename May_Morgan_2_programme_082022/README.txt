README : Guide d'utilisation de l'application de détection de race de chien :

Cette application est conçue pour être déployée et utilisée localement; sur votre ordinateur.

Le point d'entrée de cette application est donc votre invite de commande.

Les fichiers de ce dossier ont le rôle suivant :
- Le fichier "app.py" est le script python contenant l'application.
- Le fichier "ResNet50_pretrained_2.h5" est le réseau de neurones Keras entraîné, utilisé par "app.py".
- Le fichier "dict_classes.pkl" est un fichier de mapping utilisé par "app.py" et lui permettant de déterminer la race de chien prédite par le modèle.

Etapes :

1. Ouvrez une invite de commande (raccourci sur Windows : touche Windows, tapez "cmd" puis OK)

2. Placez vous dans le répertoire où se trouve l'application (sous-dossier nommé "May_Morgan_2_programme_082022") 
   (sous Windows : dans l'invite de commande  : "cd" + chemin d'accès du dossier sur votre ordinateur

3. Lancez l'application via la commande "python app.py". L'application sera alors déployée en local à l'adresse "http://127.0.0.1:5000/".

4. Pour l'utiliser, ouvrez une autre invite de commande et envoyez une requête CURL à cette adresse telle que les suivantes (en remplaçant le chemin de l'image d'entrée par celle que vous souhaitez) :
   Note : attention à bien indiquer des doubles slashes inversés \\ dans le chemin de l'image 
   
curl -X GET http://127.0.0.1:5000/predict_breed -H "Content-Type: application/json" -d "{\"input\":\"C:\\Users\\may81\\Data Science Projects\\OpenClassroom\\Projet 6 - Classez des images avec des algorithmes de Deep Learning\\Images\\n02106166-Border_collie\\n02106166_549.jpg\"}"

curl -X GET http://127.0.0.1:5000/predict_breed -H "Content-Type: application/json" -d "{\"input\":\"C:\\Users\\may81\\Data Science Projects\\OpenClassroom\\Projet 6 - Classez des images avec des algorithmes de Deep Learning\\Images\\n02096294-Australian_terrier\\n02096294_160.jpg\"}"