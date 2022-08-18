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
vanilla_advancements_dir = path.join(simple_blocks_dir, "data/minecraft/advancements/recipes/building_blocks")
functions_dir = path.join(simple_blocks_dir, "data/simple_blocks/functions")

with open(path.join(source_recipes_dir, name + ".csv"), newline="") as csv:
    csv_reader = reader(csv)
    header = next(csv_reader)
    # Header has Type, Output Item, Output Count, Input x9

    with open(path.join(functions_dir, "setup.mcfunction"), "w") as setup_function:
        setup_function.write("gamerule doLimitedCrafting true\nadvancement grant @s from minecraft:recipes/root")

    for row in csv_reader:
        type = row[0]
        output_item = row[1]
        output_count = row[2]
        input_1 = row[3]

        if type == "custom":
            continue
        elif type == "vanilla_crafting":
            continue
        elif type == "vanilla_crafting_void":
            structure = recipe_utils.advancement_void()
            dir = vanilla_advancements_dir
            filename = output_item + ".json"

            with open(path.join(functions_dir, "setup.mcfunction"), "a") as setup_function:
                setup_function.write("\nadvancement revoke @s only minecraft:recipes/building_blocks/" + output_item)
        elif type == "vanilla_stonecutter":
            structure = recipe_utils.stonecutting(output_item, int(output_count), input_1)
            dir = vanilla_recipes_dir
            filename = output_item + "_from_" + input_1 + "_stonecutting.json"
        elif type == "vanilla_stonecutter_void":
            structure = recipe_utils.advancement_void()
            dir = vanilla_advancements_dir
            filename = output_item + "_from_" + input_1 + "_stonecutting.json"

            with open(path.join(functions_dir, "setup.mcfunction"), "a") as setup_function:
                setup_function.write("\nadvancement revoke @s only minecraft:recipes/building_blocks/" + output_item + "_from_" + input_1 + "_stonecutting")
        elif type == "crafting":
            continue
        elif type == "stonecutter":
            structure = recipe_utils.stonecutting(output_item, int(output_count), input_1)
            dir = custom_recipes_dir
            filename = output_item + "_from_" + input_1 + "_stonecutting.json"
        else:
            print("Skipping recipe of type " + type + " with output item " + output_item + ".")
            continue

        json_structure = json.dumps(structure, indent=4)

        with open(path.join(dir, filename), "w") as file_out:
            file_out.write(json_structure)