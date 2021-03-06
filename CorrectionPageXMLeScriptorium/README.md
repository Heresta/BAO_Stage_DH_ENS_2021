# Correction de fichier PAGE-XML pour eScriptorium

## Mise en garde
Attention ! Pour que cela fonctionne correctement, il faut s'assurer que les namespaces qui se trouvent dans le fichier xsl correspondent à ceux qui sont dans les fichiers xml à transformer !

## Les fichiers
Dans ce dossier, vous pourrez trouver 4 fichiers. 

``automatic_correction.py`` est le fichier python qui sert à l'automatisation de la correction. Il suffit d'entrer le chemin du dossier d'origine où se trouvent 
les fichiers xml à modifier, puis le nom du dossier de sortie de cette transformation. 

``corrige.xml`` est un exemple de fichier de sortie que donne le document de transformation xsl.

``depart.xml`` est le fichier duquel par l'exemple de sortie. Celui-ci est issu des <i>Lettres</i> de Jean-Louis de Balzac publié en 1624. IL est possible de retrouver 
un exemplaire de ce livre en cliquant sur le lien suivant : https://gallica.bnf.fr/ark:/12148/btv1b86262420/f9.item.

``migrationCorrection.xsl`` est le fichier de transformation xsl. <b>Attention ! Ce document a été réalisé dans le but d'une transformation facilitant une segmentation dans <i>eScriptorium</i>. Pour cette raison, un attribut par défaut a été ajouté à chaque ligne.</b>

## Informations sur l'utilisation des fichiers
Il suffit d'avoir le fichier python et le fichier xsl dans le même dossier poour pouvoir les utiliser sans avoir à changer quoi que ce soit.

Attention ! A noter que lors des inputs pour faire tourner l'automatisation, il est nécessaire de finir son chemin par un ``/``, comme par exemple
``/home/OCR17plus-master/Data/Descartes1637_Discours_btv1b86069594_corrected/page/``.
