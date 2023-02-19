import json
from pathlib import Path
from os import path
from csv import reader

import recipe_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))

simple_blocks_dir = script.parents[2].absolute()
custom_recipes_dir = path.join(simple_blocks_dir, "data/simple_blocks/recipes")
source_recipes_dir = path.join(simple_blocks_dir, "sources/recipes")
custom_advancements_dir = path.join(
    simple_blocks_dir, "data/simple_blocks/advancements/recipes")
functions_dir = path.join(simple_blocks_dir, "data/simple_blocks/functions")

with open(path.join(source_recipes_dir, name + ".csv"), newline="") as csv:
    csv_reader = reader(csv)
    header = next(csv_reader)
    # Header has Recipe Name, Station, Category, Group, Experience, Cooking Time (Ticks), Output, Output Count, Input x9

    with open(path.join(functions_dir, "setup.mcfunction"), "w") as setup_function:
        setup_function.write(
            "advancement grant @s from simple_blocks:recipes/root")

    for row in csv_reader:
        name, station, category, group, experience, cooking_time, output, output_count = row[:8]
        inputs = row[8:]

        experience = 0 if experience == "" else float(experience)
        cooking_time = 0 if cooking_time == "" else float(cooking_time)
        output_count = 0 if output_count == "" else int(output_count)

        if station == "crafting_shaped":
            recipe_structure = recipe_utils.crafting_shaped(output, int(output_count), inputs[:9])
            filename = output
        elif station == "crafting_shapeless":
            recipe_structure = recipe_utils.crafting_shapeless(output, int(output_count), inputs[:9])
            filename = output
        elif station == "stonecutting":
            recipe_structure = recipe_utils.stonecutting(output, int(output_count), inputs[0])
            filename = output + "_from_" + inputs[0] + "_stonecutting"
        elif station == "smithing":
            recipe_structure = recipe_utils.smithing(output, output_count, inputs[:2])
            filename = output + "_smithing"
        elif station == "campfire_cooking":
            recipe_structure = recipe_utils.cooking(station, experience, cooking_time, output, inputs[0])
            filename = output + "_from_campfire_cooking"
        elif station == "smoking":
            recipe_structure = recipe_utils.cooking(station, experience, cooking_time, output, inputs[0])
            filename = output + "_from_smoking"
        elif station == "blasting":
            recipe_structure = recipe_utils.cooking(station, experience, cooking_time, output, inputs[0])
            filename = output + "_from_blasting"
        elif station == "blasting_clear":
            recipe_structure = recipe_utils.cooking("blasting", experience, cooking_time, output, inputs[0])
            filename = output + "_from_blasting_" + inputs[0]
        elif station == "smelting":
            recipe_structure = recipe_utils.cooking(station, experience, cooking_time, output, inputs[0])
            filename = output + "_from_smelting"
        elif station == "smelting_clear":
            recipe_structure = recipe_utils.cooking("smelting", experience, cooking_time, output, inputs[0])
            filename = output + "_from_smelting_" + inputs[0]
        else:
            recipe_structure = None
            print("Adding recipe with no type " + name)

        if recipe_structure is not None:
            if group != "":
                recipe_structure["group"] = group
            if category != "":
                recipe_structure["category"] = category

        if name != "":
            filename = name

        recipes_dir = custom_recipes_dir
        advancements_dir = custom_advancements_dir
        advancement_structure = recipe_utils.advancement_impossible_child_recipe(
            "simple_blocks:recipes/root", "simple_blocks:" + filename)

        if recipe_structure is not None:
            with open(path.join(recipes_dir, filename + ".json"), "w") as file_out:
                file_out.write(json.dumps(recipe_structure, indent=4))

        with open(path.join(advancements_dir, filename + ".json"), "w") as file_out:
            file_out.write(json.dumps(advancement_structure, indent=4))
