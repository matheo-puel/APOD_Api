import requests
import os 
import datetime
from deep_translator import GoogleTranslator

# Variables
CheckIcon = str("✅")
ErrorIcon = str("❌")
API_Key = "PYhivyB6uA4ZPL32UbKl3mCdlpAGhv6IviXUVXoL"
Path = "./python/Nasa/APOD_Files/"
Month_List = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Nomvenbre", "Décembre"]
Langue = "fr"

r = requests.get("https://api.nasa.gov/planetary/apod?api_key="+API_Key )
print("Requete: " + CheckIcon)
data = r.json()
print("Donées: " + CheckIcon)
# data["copyright"]
# data["date"]
# data["explanation"]
# data["hdurl"]
# data["media_type"]
# data["title"]
# data["url"]

# Traduire l'explication en Français 
Translated_Explanation = GoogleTranslator(source='auto', target=Langue).translate(data["explanation"])
# GoogleTranslator(source='auto', target=Langue).translate(data["explanation"])
print("Traduction: "+ CheckIcon)
# Récuperer la date de adj + le mois + l'année 
DateNow = datetime.date.today()
Date = DateNow.strftime("%d-%m-%Y")
Month_Int = DateNow.strftime("%m")
Month_Int = int(Month_Int) - 1

Years = DateNow.strftime("%Y")
Month = Month_List[Month_Int]
Day = DateNow.strftime("%d")

# definir le nom du fichiers 
FilePath = Path+Date+".md"

# Vérifier si le fichier pour aujourd'hui à déjà été crée et si il existe pas il le crée 
# et il crée le fichier en le remplissant.
def Loop():
    if(os.path.exists(FilePath)):
        print("Déjà ajouter: " + ErrorIcon)
        def Choice():
            DelChoice = int(input("1 Pour remplacer le fichier \n2 Pour ne rien faire \n Choix: "))
            if(DelChoice == 1):
                os.remove(FilePath)
                Loop()
            elif(DelChoice == 2):
                exit
            elif(DelChoice > 2):
                print("Erreur: Choix invalide")
        Choice()
    else:
        f = open(FilePath, "a")
        f.write("# "+data["title"])
        if data["media_type"] == "image":
            f.write("\n\n[![Build Status]("+data["url"]+")]("+data["hdurl"]+")")
            f.write("\n Cliquez sur la photo pour la voir en Ultra HD")
        else:
            f.write("\n\n## Vidéo: " + data["url"])

        f.write("\n\n- Date: "+ Date)
        if(len(data) >= 8):
            f.write("\n- Copyright: "+ data["copyright"])
        else:
            f.write("\n- Copyright: No copyright")
        f.write("\n\n## Explanation")
        f.write("\n - "+ Translated_Explanation)
        f.close()
        print("Création du fichier: " + CheckIcon)
        print("Fichier: "+ FilePath)
Loop()