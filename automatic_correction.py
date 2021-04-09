#import des librairies nécessaires
import os
import click
import re
from lxml import etree as ET
import errno
#récupérer le dossier à transformer
chemin = input("entrez le chemin du dossier: ")
dossier_resultat = input("entrez le chemin du dossier résultat: ")
if not os.path.exists(os.path.dirname(dossier_resultat)):
    try:
        os.makedirs(os.path.dirname(dossier_resultat))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
for fichier in os.listdir(chemin):
    original = ET.parse(fichier)

    transformation_xlst = ET.XSLT(ET.parse("./transformation_xml_corrige_escriptorium.xsl"))

    propre = transformation_xlst(original)

    with open('./nettoyage/'+fichier, mode='wb') as f:
        f.write(propre)