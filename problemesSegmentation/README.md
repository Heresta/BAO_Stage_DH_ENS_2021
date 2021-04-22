# Problèmes de segmentation dans des ouvrages imprimés du XVII<sup><b>e</b></sup> siècle et dans des catalogues imprimés du XIX<sup><b>e</b></sup> siècle
 
## Introduction
Dans les projets sur lesquels nous travaillons, nous avons un véritable besoin de la segmentation. Cela est avant tout nécessaire pour la transcription, mais également pour des questions de récupération de coordonnées dans la page. C'est notamment le cas si on veut isoler des illustrations ou décorations, mais aussi si on souhaite ne travailler que sur du texte et laisser de côté les numéros de page...

C'est dans ce cadre que nous pensons notre segmentation. Nous avons l'objectif d'une segmentation simple qui peut être maîtrisée par une machine grâce à un modèle entraîné dans l'application eScriptorium. De plus, afin d'essayer d'uniformiser au maximum notre segmentation - et par la suite tout document qui sera traité par le modèle créé -, nous utilisons la nomenclature du projet [SegmOnto](https://github.com/SegmOnto/examples), que ce soit pour les [zones](https://github.com/SegmOnto/examples/tree/main/zones) ou pour les [lignes](https://github.com/SegmOnto/examples/tree/main/lines).

Seulement, cette nomenclature est en cours d'élaboration et sa documentation ne répond donc pas à tous les cas de figure auxquels nous pouvons faire face. Il est aussi la question de l'utilisation d'eScriptorium qui pose des problématiques quant à l'état du fichier de sortie suite à la segmentation.

Dans ce dossier, sont centralisées les questions que nous avons au cours de la préparation de données qui donneront les datasets d'entrainements de nos modèles de segmentation.

## Fonctionnement du dossier
Dans ce dossier se trouve un fichier csv intitulé ``recap_problemes.csv`` ainsi qu'un dossier ``img``.

### Dossier ``img``
Ce dossier contient les impressions d'écran du ou des problèmes. Ceux-ci sont catégorisés dans le fichier csv.
A noter que les images sont en format png et qu'elles sont intitulées de telle manière à ce qu'elles soient rapprochables du document csv.

### Fichier ``recap_problemes.csv``
Dans ce fichier sont récapitulés les problèmes rencontrés dans la segmentation des imprimés.

Le tableau est formulé avec ces informations :
<table>
    <thead>
        <tr>
          <th>Id</th>
          <th>Nom de fichier</th>
          <th>Lien vers l’image dans le GitHub</th>
          <th>Couleurs : zones</th>
          <th>Problème</th>
          <th>Notes</th>
          <th>Résolution</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>page_titre_Boyer_Meduse_1697.png</td>
          <td>https://github.com/Heresta/BAO_Stage_DH_ENS_2021/blob/Probl%C3%A8mes-segmentation/problemesSegmentation/img/page_titre_Boyer_Meduse_1697.png</td>
          <td>Bleu : Title
              Magenta : Main
              Vert : Stamp
              Bleu ciel : Decoration</td>
          <td>Est-ce que toute la page est une zone title?</td>
          <td>None</td>
          <td>None</td>
        </tr>
    </tbody>
</table>

A noter que le séparateur est la virgule et qu'il est préférable de formater les champs entre guillemets comme texte.

Ainsi, afin de faciliter son utilisation ce fichier prend un id par problème. Nous sommes conscients qu'il peut y avoir plusieurs problèmes par image : nous proposons d'avoir une ligne par problème et non une ligne par image afin de pouvoir bien traiter tout cela. Il n'en reste pas moins que pour faciliter la récupération de l'image son nom doit être reproduit à l'identidique dans le fichier et le lien vers sa copie dans le dossier ``img`` doit être présent. Il est important également de bien préciser à quelle zone correspond chaque couleur afin de ne pas s'y perdre puisque les couleurs sont différentes selon les utilisateurs sur eScriptorium.

A noter que nous utilisons None dans une cellule vide. 
