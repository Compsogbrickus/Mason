import json
from pathlib import Path
from os import path
from csv import reader

import recipe_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))

simple_blocks_dir = script.parents[2].absolute()
vanilla_recipes_dir = path.join(simple_blocks_dir, "data/minecraft/recipes")
custom_recipes_dir = path.join(simple_blocks_dir, "data/simple_blocks/recipes")
source_recipes_dir = path.join(simple_blocks_dir, "sources/recipes")

with open(path.join(source_recipes_dir, name + ".csv"), newline="") as csv:
    csv_reader = reader(csv)
    header = next(csv_reader)

    for row in csv_reader:
        structure = recipe_utils.stonecutting(row[0], row[1], int(row[2]))

        json_structure = json.dumps(structure, indent=4)

        with open(path.join(vanilla_recipes_dir, row[1] + "_from_" + row[0] + "_stonecutting.json"), "w") as file_out:
            file_out.write(json_structure)