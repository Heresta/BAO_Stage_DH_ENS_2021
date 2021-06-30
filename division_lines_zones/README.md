# Calcul du nombre de zones et de lignes par type dans les documents XML ALTO

## A quoi correspond chaque programme ?

### computation_all_documents.py

Ce programme permet d'avoir un aperçu global de la quantité de zones par type
et de lignes par type qui existent dans tous les documents différents d'un 
corpus.

Il donne en sortie un fichier texte, qui sera conservé dans un dossier nommé
`results`, lui-même conservé dans le dossier du programme.

### computation_document.py

Ce programme permet d'avoir un aperçu par document dans un corpus 
de la quantité de zones par type et de lignes par type qui existent.

Il donne en sortie un fichier texte, qui sera conservé dans un dossier nommé  
`results`, lui-même conservé dans le dossier du programme.

### computation_lines_by_zone.py

Ce programme permet d'avoir un aperçu pour tous les documents dans un corpus 
de la quantité de type de lignes par type de  zones qui existent.

Il donne en sortie un fichier texte, qui sera conservé dans un dossier nommé
`results`, lui-même conservé dans le dossier du programme.

## Comment utiliser ces programmes

Attention ! Ces programmes fonctionnent pour un calcul sur plusieurs fichiers
dans plusieurs dossiers différents intégrés dans un seul dossier. Ainsi pour 
utiliser ces programmes, il faut télécharger celui ou ceux dont vous avez besoin
et utiliser une ligne de commande comme suit :

`python [nom du fichier du programme] [chemin jusqu'à la division entre les 
différents dossiers] [en option : - f suivi de la fin du chemin à l'intérieur
de chaque dossier (attention à ce que les noms des dossiers soient les mêmes)]`

Attention ! Ce programme est basé sur l'utilisation de l'ontologie [SegmOnto](https://github.com/SegmOnto/examples).
Si vous n'utilisez pas cela, les programmes seront à adapter à votre vocabulaire.

