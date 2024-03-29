# Copyright 2023 Compsogbrickus
# SPDX-License-Identifier: Apache-2.0

import json
from pathlib import Path
from os import path, makedirs
from shutil import rmtree
from contextlib import ExitStack
from csv import reader

import recipe_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))

mason_dir = script.parents[2].absolute()
custom_recipes_dir = path.join(mason_dir, "data/mason/recipes")
source_recipes_dir = path.join(mason_dir, "sources/recipes")
functions_dir = path.join(mason_dir, "data/mason/functions")

give_recipes_dir = path.join(functions_dir, "give_recipes")
take_recipes_dir = path.join(functions_dir, "take_recipes")

recipe_types = ["crafting_shaped_small",
                "crafting_shaped_large",
                "crafting_shapeless_small",
                "crafting_shapeless_large",
                "stonecutting",
                "smithing_transform",
                "smithing_trim",
                "campfire_cooking",
                "smoking",
                "blasting",
                "smelting",
                "other"]

for dir in [custom_recipes_dir, give_recipes_dir, take_recipes_dir]:
    if path.exists(dir):
        rmtree(dir)
    makedirs(dir)

with ExitStack() as stack:
    csv = stack.enter_context(open(path.join(source_recipes_dir, name + ".csv"), newline=""))
    give_recipes = [stack.enter_context(open(path.join(give_recipes_dir, fname + ".mcfunction"), "w")) for fname in recipe_types]
    take_recipes = [stack.enter_context(open(path.join(take_recipes_dir, fname + ".mcfunction"), "w")) for fname in recipe_types]

    csv_reader = reader(csv)
    header = next(csv_reader)
    # Header has Recipe Name, Station, Category, Group, Experience, Cooking Time (Ticks), Output, Output Count, Inputs

    for row in csv_reader:
        name, station, category, group, experience, cooking_time, output, output_count = row[:8]
        inputs = row[8:]

        experience   = 0 if experience   == "" else float(experience)
        cooking_time = 0 if cooking_time == "" else float(cooking_time)
        output_count = 0 if output_count == "" else int(output_count)

        if station == "crafting_shaped":
            recipe_structure = recipe_utils.crafting_shaped(output, int(output_count), inputs[:9])
            
            pattern_rows = recipe_structure.get("pattern", "")
            height = len(pattern_rows)
            width = len(pattern_rows[0])

            if (height < 3) and (width < 3):
                id = 0
            else:
                id = 1

            filename = output
        elif station == "crafting_shapeless":
            inputs_length, recipe_structure = recipe_utils.crafting_shapeless(output, int(output_count), inputs[:9])
            
            if inputs_length < 5:
                id = 2
            else:
                id = 3
            
            filename = output
        elif station == "stonecutting":
            recipe_structure = recipe_utils.stonecutting(output, int(output_count), inputs[0])

            id = 4

            filename = output + "_from_" + inputs[0] + "_stonecutting"
        elif station == "smithing_transform":
            recipe_structure = recipe_utils.smithing_transform(output, output_count, inputs[:3])

            id = 5

            filename = output + "_smithing"
        elif station == "smithing_trim":
            recipe_structure = recipe_utils.smithing_trim(inputs[:3])

            id = 6

            filename = inputs[0] + "_smithing_trim"
        elif station == "campfire_cooking":
            recipe_structure = recipe_utils.cooking(station, experience, cooking_time, output, inputs[0])

            id = 7

            filename = output + "_from_campfire_cooking"
        elif station == "smoking":
            recipe_structure = recipe_utils.cooking(station, experience, cooking_time, output, inputs[0])

            id = 8

            filename = output + "_from_smoking"
        elif (station == "blasting"):
            recipe_structure = recipe_utils.cooking(station, experience, cooking_time, output, inputs[0])

            id = 9

            filename = output + "_from_blasting"
        elif station == "blasting_clear":
            recipe_structure = recipe_utils.cooking("blasting", experience, cooking_time, output, inputs[0])

            id = 9

            filename = output + "_from_blasting_" + inputs[0]
        elif station == "smelting":
            recipe_structure = recipe_utils.cooking(station, experience, cooking_time, output, inputs[0])

            id = 10

            filename = output + "_from_smelting"
        elif station == "smelting_clear":
            recipe_structure = recipe_utils.cooking("smelting", experience, cooking_time, output, inputs[0])

            id = 10

            filename = output + "_from_smelting_" + inputs[0]
        else:
            recipe_structure = None

            id = -1

            print("Adding recipe with no type " + name)

        if name != "":
            filename = name
        
        if recipe_structure is not None:
            if group != "":
                recipe_structure["group"] = group
            if category != "":
                recipe_structure["category"] = category
            recipe_structure["show_notification"] = False
            
            with open(path.join(custom_recipes_dir, filename + ".json"), "w") as file_out:
                file_out.write(json.dumps(recipe_structure, indent=4))

        give_recipes[id].write("recipe give @s mason:" + filename + "\n")
        take_recipes[id].write("recipe take @s mason:" + filename + "\n")
