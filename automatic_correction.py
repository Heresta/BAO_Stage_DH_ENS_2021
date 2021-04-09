#import des librairies nécessaires
import os
import click
import re
from lxml import etree as ET
from bs4 import BeautifulSoup

#récupérer le dossier à transformer
#chemin = input("entrez le chemin du dossier: ")
path = './Balzac1624_Lettres_btv1b86262420_corrected_0011.xml'

original = ET.parse(path)

transformation_xlst = ET.XSLT(ET.parse("./transformation_xml_corrige_escriptorium.xsl"))

propre = transformation_xlst(original)

with open('final.xml', mode='wb') as f:
    f.write(propre)


#parser la feuille de transformation


#lancer la feuille sur les différents fichiers du dossier

#faire la version en CLI
