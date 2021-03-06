# Boite à outils dans le cadre d'un stage à l'ENS de Paris
Cette boite à outils a été créée dans l'optique de donner accès à tous aux outils que nous avons conçus dans le cadre de notre stage à l'ENS de Paris.

## Sommaire
### Dossier - Automatisation_copie_fichiers
Ce dossier contient plusieurs scripts Python qui ont pour but d'automatiser la création et le remplissage de dossiers de dataset. [En savoir plus (README)](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/blob/Automatisation_copie_fichiers/main/README.md)

[Lien vers le dossier ``Automatisation_copie_fichiers``](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/tree/main/Automatisation_copie_fichiers)

_Créé par [@Heresta](http://github.com/Heresta)_

### Dossier - CorrectionPageXMLeScriptorium
Ce dossier contient un script Python ainsi qu'une feuille de transformation xsl qui ont pour but de normaliser des fichiers PAGE-XML afin de pouvoir les utiliser sans soucis dans l'application eScriptorium. [En savoir plus (README)](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/blob/main/CorrectionPageXMLeScriptorium/README.md)

[Lien vers le dossier ``CorrectionPageXMLeScriptorium``](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/tree/main/CorrectionPageXMLeScriptorium)

_Créé par [@Heresta](http://github.com/Heresta) et [@Juliettejns](http://github.com/Juliettejns)_

### Dossier - RetraitTranscriptionPAGEXML
Ce dossier contient un script Python ainsi qu'une feuille de transformation xsl qui ont pour but de partir d'un fichier xml sortant d'eScriptorium pour en enlever les transcriptions et en faire un simple fichier de segmentation. Cela a pour but d'aider les tests sur les modèles de recognizer d'eScriptorium tant que l'on n'a pas de modèle de segmentation qui fonctionne. [En savoir plus (README)](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/blob/main/RetraitTranscriptionPAGEXML/README.md)

[Lien vers le dossier ``RetraitTranscriptionPAGEXML``](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/tree/main/RetraitTranscriptionPAGEXML)

_Créé par [@Heresta](http://github.com/Heresta)_

### Dossier - division_lines_zones

Ce dossier contient trois programmes CLI python qui permettent de récupérer des statistiques de quantités de type de zones et de lignes dans un fichier ALTO4.
Attention ! A noter que ces programmes sont à adapter si le vocabulaire utilisé n'est pas celui de [SegmOnto](https://github.com/SegmOnto).
[En savoir plus (README)](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/blob/main/division_lines_zones/README.md)

_Créé par [Heresta](http://github.com/Heresta)_

### Dossier - documentationFormatsExistants
Ce dossier contient quatre fichiers xml commentés en français en fonction de leur documentation, de notre utilisation et de notre compréhension. Ils présentent plusieurs formats : 
- ALTO
  - version 2
  - version 4
- PAGE-XML
  - en sortie de l'application Transkribus
  - en sortie de l'application eScriptorium

[Lien vers le dossier ``documentationFormatsExistants``](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/tree/main/documentationFormatsExistants)

_Créé par [@Heresta](http://github.com/Heresta) et [@Juliettejns](http://github.com/Juliettejns)_

### Dossier - problemesSegmentation
Ce dossier contient un fichier csv ainsi qu'un dossier d'images qui ont pour but de répertorier les problématiques recontrées lors de la segmentation d'imprimés du XVII<sup>e</sup> et du XIX<sup>e</sup> siècle. [En savoir plus (README)](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/blob/Probl%C3%A8mes-segmentation/problemesSegmentation/README.md)

[Lien vers le dossier ``problemesSegmentation``](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/tree/Probl%C3%A8mes-segmentation/problemesSegmentation)

_Créé et complété par [@Heresta](http://github.com/Heresta) et [@Juliettejns](http://github.com/Juliettejns)_

### Fichier Python - creationCSVDataset.py
Ce fichier est un petit script qui permet de récupérer directement les noms des fichiers dans d'un dossier de dataset dans un fichier csv.

_Attention à bien modifier les chemins indiqués dans le document!_

[Lien vers le fichier ``creationCSVDataset.py``](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/blob/main/creationCSVDataset.py)

_Créé par [@Juliettejns](http://github.com/Juliettejns)_

### Fichier Python - suppressionGrasItalique.py
Ce fichier est un petit script qui a pour but d'automatiser la suppression des balises ``<b>`` et ``<i>`` des documents PageXML.
  
[Lien vers le fichier ``suppressionGrasItalique.py``](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/blob/main/suppressionGrasItalique.py)  
  
_Créé par [@Juliettejns](http://github.com/Juliettejns)_

## Crédits
Ce repository est un dossier de travail administré par [@Heresta](http://github.com/Heresta) et [@Juliettejns](http://github.com/Juliettejns) avec l'aide  de Simon Gabay et sous la supervision de Béatrice Joyeux-Prunel. 

Il correspond au travail effectué lors du stage de fin d'études du master Technologies Numériques appliquées à l'Histoire de l'Ecole nationale des Chartes, réalisé dans le cadre du centre IMAGO et du projet ARTL@s.

## Licence
Ce repository est CC-BY.
![68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f6c2f62792f322e302f38387833312e706e67](https://user-images.githubusercontent.com/56683417/115237678-2150d080-a11d-11eb-903e-5a26587e12e1.png)
