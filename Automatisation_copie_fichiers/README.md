# Automatisation de copie de fichiers

## Les fichiers
Dans ce dossier, vous pourrez trouver 2 fichiers Python. 

``copie_fichiers_xml.py`` est un fichier python qui sert à l'automatisation de la copie de fichier xml vers un autre dossier que celui où ils se trouvent. Cela permet de créer un dataset selon un dossier avec les png à utiliser.

``fichier_hasard.py`` est un programme permettant de créer un dossier avec un certain nombre de fichiers au hasard provenant d'un autre dossier (création de dataset au hasard).

## Informations sur l'utilisation des fichiers
Il suffit de bien changer les chemins indiqués dans les fichiers afin de les adapter aux vôtres.

A noter qu'il n'est pas nécessaire d'avoir un fichier destination bien réel : les deux scripts peuvent vous le créer.

Dans ``fichier_hasard.py``, il est important de bien changer si besoin les arguments de la fonction ``numpy.random.choice(liste_fichier_png, 30, False)``. Les commentaires du script comportent toutes les informations à ce sujet.

ATTENTION : le package ``numpy`` peut être à télécharger si cela n'a pas été déjà fait sur votre ordinateur ou dans l'environnement que vous utilisez.
