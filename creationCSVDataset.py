"""
Programme permettant de récupérer les noms des fichiers d'un dossier en d'en faire un csv 
afin de créer rapidement un csv de suivi de construction d'un dataset
Auteur: Juliette Janes  
Date: 18/04/20
"""
import os
import csv

dossier = "./travail_test_segmentation/"
liste_fichier=[]
for fichier in os.listdir(dossier):
    liste_fichier.append(fichier)
with open("Dataset_190421.csv", "w") as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    for word in liste_fichier:
        wr.writerow([word])
