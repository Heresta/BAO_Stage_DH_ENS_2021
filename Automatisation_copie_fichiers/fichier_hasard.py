"""
Programme permettant de créer un dossier avec un certain nombre de fichiers au hasard 
provenant d'un autre dossier (création de dataset au hasard)
Auteur: Claire Jahan (Heresta)  
Date: 27/04/21
"""

from shutil import copy

import os
import numpy

# dossier avec les png du dataset
dossier_png = "./png/"
dossier_resultat = "./nouveau_png/"

# vérification du dossier de résultat + si non existence, création
if not os.path.exists(os.path.dirname(dossier_resultat)):
    try:
        os.makedirs(os.path.dirname(dossier_resultat))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

liste_fichier_png = []

# remplissage de la liste d'images
for fichier in os.listdir(dossier_png):
    liste_fichier_png.append(fichier)

# liste avec les noms des fichiers choisis au hasard
# dans les arguments : liste_fichier_png = liste avec tous les noms des images ; 
# dans les arguments : 30 = le nombre de fichiers au hasard désiré ; 
# dans les arguments : False = n'avoir que des références uniques
random = numpy.random.choice(liste_fichier_png, 30, False)

for fichier in liste_fichier_png:
    if fichier in random:
        copy(dossier_png+fichier,dossier_resultat)
