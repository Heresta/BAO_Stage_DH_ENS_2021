# Automatisation du retrait de la transcription des fichiers PAGE-XML sortant d'eScriptorium
Pour information, ces script python et de transformation xslt sont largement basés sur ceux qui se trouvent dans le dossier [CorrectionPageXMLeScriptorium](https://github.com/Heresta/BAO_Stage_DH_ENS_2021/tree/main/CorrectionPageXMLeScriptorium).

## Les fichiers
Dans ce dossier, vous pourrez trouver 4 fichiers. 

``xml_segment_only.py`` est le fichier python qui sert à l'automatisation de la transformation. Il suffit d'entrer le chemin du dossier d'origine où se trouvent 
les fichiers xml à modifier, puis le nom du dossier de sortie de cette transformation. 

``arrivee.xml`` est un exemple de fichier de sortie que donne le document de transformation xsl.

``depart.xml`` est le fichier duquel part l'exemple de sortie. Celui-ci est issu des _Caractères_ de Jean de La Bruyère publié en 1688. Il est possible de retrouver 
un exemplaire de ce livre en cliquant sur le lien suivant : https://gallica.bnf.fr/ark:/12148/btv1b86070385/f14.item.

``retrait_transcription.xsl`` est le fichier de transformation xsl. <b>Attention ! Ce document a été réalisé avec un certain type de namespace. Il faut absolument vérifier que le namespace du document xsl est le même que celui du document PAGE-XML que vous souhaitez traiter. Dans le cas contraire, il suffit de le modifier pour que la transformation fonctionne.</b>

## Informations sur l'utilisation des fichiers
Il suffit d'avoir le fichier python et le fichier xsl dans le même dossier poour pouvoir les utiliser sans avoir à changer quoi que ce soit.

Attention ! A noter que lors des inputs pour faire tourner l'automatisation, il est nécessaire de finir son chemin par un ``/``, comme par exemple
``/home/OCR17plus-master/Data/Descartes1637_Discours_btv1b86069594_corrected/page/``.
