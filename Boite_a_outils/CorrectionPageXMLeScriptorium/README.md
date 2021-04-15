# Correction de fichier PAGE-XML pour eScriptorium

## Les fichiers
Dans ce dossier, vous pourrez trouver 4 fichiers. 

``automatic_correction.py`` est le fichier python qui sert à l'automatisation de la correction. Il suffit d'entrer le chemin du dossier d'origine où se trouvent 
les fichiers xml à modifier, puis le nom du dossier de sortie de cette transformation. 

``corrige.xml`` est un exemple de fichier de sortie que donne le document de transformation xsl.

``depart.xml`` est le fichier duquel par l'exemple de sortie.

``migrationCorrection.xsl`` est le fichier de transformation xsl.

## Informations sur l'utilisation des fichiers
Il suffit d'avoir le fichier python et le fichier xsl dans le même dossier poour pouvoir les utiliser sans avoir à changer quoi que ce soit.

Attention ! A noter que lors des inputs pour faire tourner l'automatisation, il est nécessaire de finir son chemin par un ``/``, comme par exemple
``/home/OCR17plus-master/Data/Descartes1637_Discours_btv1b86069594_corrected/page/``.
