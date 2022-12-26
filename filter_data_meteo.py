#!/usr/bin/python

#Importation des librairies standards 
import pandas as pd 
import sys 
import json 
import requests


#Liste des vetements pour les femmes  proposes selon la temperature 
habille_froid_femme=["un bonnet","des gants", "un col roule", "un jeans", "des bottines", "un manteau"]
habille_tempere_femme=["un pull","une jupe", "un collant", "une paire de mocassin", "une veste"]
habille_chaud_femme=["une robe", "une paire de sandale"]

#Liste des vetements pour les hommes  proposes selon la temperature 
habille_froid_homme=["des gants", "un bonnet", "un col roule","un pantalon","une paire de bottine","une doudoune"]
habille_tempere_homme=["une chemise", "un jean","une veste","une paire de basket"]
habille_chaud_homme=["un t-shirt", "un bermuda", "une paire de basket"]


# Fonction de recommandation selon le sexe et la temperatures entrees
def todayOutfit(temperature_actuelle,sexe):
  if sexe == "F":
    if float(temperature_actuelle) <= 11.0:
      print("L'oufit du jour pourrait etre : " + str(habille_froid_femme))
    elif 11.0 < float(temperature_actuelle) <= 25.0:
      print( "L'oufit du jour pourrait etre : " + str(habille_tempere_femme))
    else:
      print("L'oufit du jour pourrait etre : " + str(habille_chaud_femme))
  else:
      if float(temperature_actuelle) <= 11.0:
        print("L'oufit du jour pourrait etre : " + str(habille_froid_homme))
      elif 11.0 <  float(temperature_actuelle) <= 25.0:
        print("L'oufit du jour pourrait etre : " + str(habille_tempere_homme))
      else:
        print("L'oufit du jour pourrait etre : " + str(habille_chaud_homme))

  return "Merci d'avoir utiliser TODAY'S OUTFIT"

isAutomatic=input("Souhaitez-vous une recommandation automatique de l'outfit du jour ? ")
if isAutomatic == 'Y':
  # Recuperation du sexe de l'utilisateur
  sexe =str(input("Entrez votre sexe : "))
  # Recuperation des donnees meteorologiques de Paris par un appel API sur le site Open meteo
    ## Stockage de  l'URL de l'endroit de recuperation des donnees 
  URL = "https://api.open-meteo.com/v1/forecast?latitude=48.52&longitude=2.333333&current_weather=true"

  ## Stockage du fichier json contenant la temperature actuelle
  print("La collecte de la temperature est en cours... Merci de patienter")
  get_data = requests.get(url=URL)

  ## Parsing du fichier json et stockage dans une variable
  data=get_data.json()
  temperature_actuelle = data['current_weather']['temperature']
  print("La temperature actuelle est : " + str(temperature_actuelle))

  # Recommandation selon le sexe et la temperature
  print(todayOutfit(temperature_actuelle,sexe))

# Recommandation manuelle de l'outfit
elif isAutomatic == 'N':
  ## Recuperation manuelle de la temperature actuelle
  temperature_actuelle=input("Entrez la temperature actuelle : ")
  ## Recuperation du sexe de l'utilisateur
  sexe =str(input("Entrez votre sexe : "))
  print(todayOutfit(temperature_actuelle,sexe))

else:
  print("Selection incorrecte, veuillez entrez Y ou N")