import json
from pathlib import Path
from os import path
from csv import reader

import recipe_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))
dir = script.parent.absolute()

with open(path.join(dir, name + ".csv"), newline="") as csv:
    csv_reader = reader(csv)
    header = next(csv_reader)
    for row in csv_reader:
        structure = recipe_utils.stonecutting(row[0], row[1], int(row[2]))

        json_structure = json.dumps(structure, indent=4)

        with open(path.join(dir, row[1] + "_from_" + row[0] + "_stonecutting.json"), "w") as file_out:
            file_out.write(json_structure)