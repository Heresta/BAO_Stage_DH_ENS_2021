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