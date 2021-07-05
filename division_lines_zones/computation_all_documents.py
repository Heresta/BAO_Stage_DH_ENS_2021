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

    zone = {"Title": 0, "Main": 0, "Damage": 0, "Decoration": 0, "DropCapital": 0, "Figure": 0, "Margin": 0,
            "Numbering": 0, "MusicNotation": 0, "RunningTitle": 0, "Seal": 0, "Signatures": 0, "Stamp": 0,
            "Table": 0}
    line = {"Default": 0, "DropCapitalLine": 0, "Interlinear": 0, "MusicLine": 0, "Rubric": 0}

    fichier_final_nom = "datasetsOCRSegmenter17"
    for directory in os.listdir(dossier):
        for fichier in os.listdir(dossier + directory + fin_chemin):
            file = ET.parse(dossier + directory + fin_chemin + fichier)
            root = file.getroot()
            layout = root[2]
            for page in layout:
                for printspace in page:
                    for textblock in printspace:
                        for item in root[1]:
                            if textblock.get("TAGREFS") == item.get("ID"):
                                for ref in tag_label["textblock"]:
                                    if ref[1] == item.get("LABEL"):
                                        zone[item.get("LABEL")] += 1
                        for textline in textblock:
                            if textline.tag == "{http://www.loc.gov/standards/alto/ns-v4#}TextLine":
                                for item in root[1]:
                                    if textline.get("TAGREFS") == item.get("ID"):
                                        for re in tag_label["textline"]:
                                            if re[1] == item.get("LABEL"):
                                                line[item.get("LABEL")] += 1

    zone_final = {}
    line_final = {}
    for item, value in zone.items():
        if value != 0:
            zone_final[item] = value
    for item, value in line.items():
        if value != 0:
            line_final[item] = value

    with open("./results/" + fichier_final_nom + '.txt', 'w') as f:
        zones = zone_final.values()
        lines = line_final.values()
        total_zone = 0
        total_line = 0
        for item in zones:
            total_zone += item
        for item in lines:
            total_line += item
        f.writelines("## About files' segmentation\n\n")
        f.writelines("### About zones:\n\n")
        for nom, valeur in zone_final.items():
            f.writelines(
                [nom + ": " + str(valeur) + " (" + str(round(valeur / total_zone * 100, 2)) + "%)" + "\n\n"])
        f.writelines("### About lines:\n\n")
        for nom, valeur in line_final.items():
            f.writelines(
                [nom + ": " + str(valeur) + " (" + str(round(valeur / total_line * 100, 2)) + "%)" + "\n\n"])


if __name__ == "__main__":
    calcul()