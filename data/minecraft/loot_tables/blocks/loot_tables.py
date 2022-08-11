import json
from pathlib import Path
from os import path
from csv import reader

import loot_table_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))
dir = script.parent.absolute()

with open(path.join(dir, name + ".csv"), newline="") as csv:
    csv_reader = reader(csv)
    header = next(csv_reader)
    for row in csv_reader:
        if row[1] == "":
            structure = loot_table_utils.blocks_empty()
        else:
            structure = loot_table_utils.blocks(row[0], row[1], int(row[2]))

        json_structure = json.dumps(structure, indent=4)

        with open(path.join(dir, row[0] + ".json"), "w") as file_out:
            file_out.write(json_structure)