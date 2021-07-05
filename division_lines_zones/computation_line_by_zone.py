from lxml import etree as ET
import click
import os
import errno


@click.command("calcul")
@click.argument("dossier")
@click.argument("fin_chemin")
def calcul(dossier, fin_chemin):
    if not os.path.exists(os.path.dirname("./results/")):
        try:
            os.makedirs(os.path.dirname("./results/"))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    tag_label = {"textblock": [["BT1", "Title", "block type Title"],
                               ["BT2", "Main", "block type Main"],
                               ["BT3", "Damage", "block type Damage"],
                               ["BT4", "Decoration", "block type Decoration"],
                               ["BT5", "DropCapital", "block type DropCapital"],
                               ["BT6", "Figure", "block type Figure"],
                               ["BT7", "Margin", "block type Margin"],
                               ["BT8", "Numbering", "block type Numbering"],
                               ["BT9", "MusicNotation", "block type MusicNotation"],
                               ["BT10", "RunningTitle", "block type RunningTitle"],
                               ["BT11", "Seal", "block type Seal"],
                               ["BT12", "Signatures", "block type Signatures"],
                               ["BT13", "Stamp", "block type Stamp"],
                               ["BT14", "Table", "block type Table"]],
                 "textline": [["LT1", "Default", "block type Default"],
                              ["LT2", "DropCapitalLine", "block type DropCapitalLine"],
                              ["LT3", "Interlinear", "block type Interlinear"],
                              ["LT4", "MusicLine", "block type MusicLine"],
                              ["LT5", "Rubric", "block type Rubric"]]}
    zone = {"Title": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "Main": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "Damage": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "Decoration": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "DropCapital": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "Figure": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "Margin": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "Numbering": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "MusicNotation": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "RunningTitle": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "Seal": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "Signatures": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "Stamp": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0},
            "Table": {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0}}
    fichier_final_nom = "datasetsOCRSegmenter17SUPPL"
    for directory in os.listdir(dossier):
        for fichier in os.listdir(dossier + directory + fin_chemin):
            file = ET.parse(dossier + directory + fin_chemin + fichier)
            root = file.getroot()
            layout = root[2]
            tag = ""
            for page in layout:
                for printspace in page:
                    for textblock in printspace:
                        for item in root[1]:
                            if textblock.get("TAGREFS") == item.get("ID"):
                                for ref in tag_label["textblock"]:
                                    if ref[1] == item.get("LABEL"):
                                        tag = ref[1]
                        for textline in textblock:
                            if textline.tag == "{http://www.loc.gov/standards/alto/ns-v4#}TextLine":
                                for item in root[1]:
                                    if textline.get("TAGREFS") == item.get("ID"):
                                        for re in tag_label["textline"]:
                                            if re[1] == item.get("LABEL"):
                                                zone[tag][re[1]] += 1
    with open("./results/" + fichier_final_nom + '.txt', 'w') as f:
        f.writelines("## About files' segmentation\n\n")
        f.writelines("### About zones:\n\n")
        for nom, valeur in zone.items():
            f.writelines([nom + ":\n\n"])
            for item2, valeur2 in valeur.items():
                if valeur2 != 0:
                    f.writelines(["- " + item2 + ": " + str(valeur2) + "\n\n"])

if __name__ == "__main__":
    calcul()