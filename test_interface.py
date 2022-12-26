#!/usr/bin/python3
import json 
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import *


root = Tk()
root.title('Todays Outfit')
root.geometry("500x480")
root.configure(bg='pink')

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
    if temperature_actuelle <= 11.0:
      label_1 = Label(root,text="L'oufit du jour pourrait etre : " + str(habille_froid_femme))
      label_1.pack()
    elif 11.0 < temperature_actuelle <= 25.0:
      label_2 = Label(root, text="L'oufit du jour pourrait etre : " + str(habille_tempere_femme))
      label_2.pack()
    else:
      label_3 =Label(root,text="L'oufit du jour pourrait etre : " + str(habille_chaud_femme))
      label_3.pack()
  else:
      if temperature_actuelle <= 11.0:
        label_4 = Label(root,text="L'oufit du jour pourrait etre : " + str(habille_froid_homme))
        label_4.pack()
      elif 11.0< temperature_actuelle <= 25.0:
        label_5 = Label(root,text="L'oufit du jour pourrait etre : " + str(habille_tempere_homme))
        label_5.pack()
      else:
	      label_6 = Label(root,text="L'oufit du jour pourrait etre : " + str(habille_chaud_homme))
	      label_6.pack()
  return "Merci d'avoir utiliser TODAY'S OUTFIT"


sexe_var_automatic = tk.StringVar()
def get_sexe_automatic():
    sexe=  Label(root, text="Entrez votre sexe : ")
    sexe.pack()
    sexe_entry = Entry(root, textvariable=sexe_var_automatic).pack()
    submit_button_automatic = Button(root, text='Submit',command=automatic_recommandation)
    return submit_button_automatic.pack()


temperature_actuelle_var = tk.StringVar()
def get_temperature_manuelle():
    temperature_actuelle_label =Label(root,text=" Entrez la temperature actuelle : ")
    temperature_actuelle_label.pack()
    temperature_actuelle_entry = Entry(root,textvariable=temperature_actuelle_var).pack()
    return temperature_actuelle_entry


sexe_var_manual = tk.StringVar()
def get_sexe_manual():
    sexe_2 = Label(root,text="Entrez votre sexe : ")
    sexe_2.pack()
    sexe_entry = Entry(root, textvariable=sexe_var_manual).pack()
    submit_button_manual = Button(root, text='Submit',command=manual_recommandation)
    return submit_button_manual.pack()


def automatic_recommandation():
    URL = "https://api.open-meteo.com/v1/forecast?latitude=48.52&longitude=2.333333&current_weather=true"
    get_data = requests.get(url=URL)
    data=get_data.json()
    temperature_actuelle = data['current_weather']['temperature']
    label_7 = tk.Label(root,text="La temperature actuelle est : " + str(temperature_actuelle))
    label_7.pack()
    sexe = sexe_var_automatic.get()
    return todayOutfit(temperature_actuelle, sexe)

def manual_recommandation():
    sexe_2 = sexe_var_manual.get()
    temperature_actuelle =float(temperature_actuelle_var.get())
    return todayOutfit(temperature_actuelle,sexe_2)



first_question = Label(root, text="Souhaiteriez-vous une recommandation manuelle ou automatique ?")
first_question.pack()
yes_button = Button(root, text = 'Yes',command=get_sexe_automatic)
yes_button.pack()
no_button = Button(root, text = 'No', command=lambda:[get_temperature_manuelle(),get_sexe_manual()])
no_button.pack()



root.mainloop()
