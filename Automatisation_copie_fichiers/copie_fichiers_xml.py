"""
Programme permettant de copier des fichiers xml d'un dossier général vers un autre dossier 
pour créer un dataset, selon les images qui sont déjà dans ce dossier de dataset
Auteur: Claire Jahan (Heresta)  
Date: 27/04/21
"""

from shutil import copy

import os
import errno

# dossier avec les png du dataset
# attention à bien mettre un / après le nom du dossier
dossier_png = "/home/tnah/Documents/Stage/training_escriptorium/training_segmenter/2.0 evaluation set/png/"
# dossier avec toutes les pages xml confondues
# attention à bien mettre un / après le nom du dossier
dossier_page_xml = "/home/tnah/Documents/Stage/training_escriptorium/training_segmenter/toutes_pages_xml/"
# dossier où se retrouveront les page-xml correspondant aux png
# attention à bien mettre un / après le nom du dossier
dossier_resultat = "/home/tnah/Documents/Stage/training_escriptorium/training_segmenter/2.0 evaluation set/PAGE_XML/"

# vérification du dossier de résultat + si non existence, création
if not os.path.exists(os.path.dirname(dossier_resultat)):
    try:
        os.makedirs(os.path.dirname(dossier_resultat))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

liste_fichier_png = []

liste_fichier_page_xml = []

# remplissage de la liste d'images
for fichier in os.listdir(dossier_png):
    liste_fichier_png.append(fichier[:-4])

# remplissage de la liste de tous les fichires page-xml
for fichier in os.listdir(dossier_page_xml):
    liste_fichier_page_xml.append(fichier[:-4])

# comparaison des deux listes puis ajout d'une copie du fichier xml dans le dossier resultat
for fichier in liste_fichier_page_xml:
    if fichier in liste_fichier_png:
        copy(dossier_page_xml+fichier+".xml", dossier_resultat)
