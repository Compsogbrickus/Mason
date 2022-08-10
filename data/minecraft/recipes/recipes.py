import json
from pathlib import Path
from os import path
from csv import reader

recipe_script = Path(__file__)
recipe_dir = recipe_script.parent.absolute()

with open(path.join(recipe_dir, "recipes.csv"), newline="") as recipes_csv:
    recipes_reader = reader(recipes_csv)
    header = next(recipes_reader)
    rows = []
    for row in recipes_reader:
        rows.append(row)

recipe = {
    "type": "minecraft:stonecutting",
    "count": 2,
    "ingredient": {
        "item": "minecraft:" + rows[4][0]
    },
    "result": "minecraft:" + rows[4][3]
}

json_recipe = json.dumps(recipe, indent=4)

with open(path.join(recipe_dir, rows[4][3] + "_from_" + rows[4][0] + "_stonecutting.json"), "w") as file_out:
    file_out.write(json_recipe)