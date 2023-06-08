# Copyright 2023 Compsogbrickus
# SPDX-License-Identifier: Apache-2.0

import json
import re
from pathlib import Path
from os import path
from csv import writer

import recipe_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))

simple_blocks_dir = script.parents[2].absolute()
vanilla_recipes_dir = path.join(simple_blocks_dir, "data/minecraft/recipes")
custom_recipes_dir = path.join(simple_blocks_dir, "data/simple_blocks/recipes")
source_recipes_dir = path.join(simple_blocks_dir, "sources/recipes")

header = ["Recipe Name", "Station", "Category", "Group", "Experience",
          "Cooking Time (Ticks)", "Output", "Output Count", "Input", "Input", "Input", "Input", "Input", "Input", "Input", "Input", "Input"]


def recipe_to_csv(csv_writer, recipe_name, loaded_recipe):
    current_recipe = json.load(loaded_recipe)

    station = current_recipe["type"].split(":")[1]

    if re.search("_from_blasting_", recipe_name):
        station = "blasting_clear"
    elif re.search("_from_smelting_", recipe_name):
        station = "smelting_clear"

    category = current_recipe.get("category", "")
    group = current_recipe.get("group", "")

    experience = ""
    cooking_time = ""

    if station == "crafting_shaped":
        output_item = recipe_utils.get_item(current_recipe["result"])
        output_count = current_recipe["result"].get("count", 1)

        inputs = []

        for line in range(len(current_recipe["pattern"])):
            while len(current_recipe["pattern"][line]) < 3:
                current_recipe["pattern"][line] += " "
            inputs += list(current_recipe["pattern"][line])

        inputs = (inputs + 6*[" "])[:9]

        for slot in range(len(inputs)):
            for key in current_recipe["key"]:
                value = recipe_utils.get_ingredient(current_recipe["key"][key])

                if inputs[slot] == key:
                    inputs[slot] = value

            if inputs[slot] == " ":
                inputs[slot] = ""
            elif len(inputs[slot]) == 1:
                print("Key mismatch found in recipe with name " + recipe_name)
    elif station == "crafting_shapeless":
        output_item = recipe_utils.get_item(current_recipe["result"])
        output_count = current_recipe["result"].get("count", 1)
        inputs = []

        for ingredient in range(len(current_recipe["ingredients"])):
            inputs.append(recipe_utils.get_ingredient(current_recipe["ingredients"][ingredient]))
    elif station == "stonecutting":
        output_item = current_recipe["result"].split(":")[1]
        output_count = current_recipe["count"]
        inputs = [recipe_utils.get_ingredient(current_recipe["ingredient"])]
    elif station == "smithing_trim":
        output_item = ""
        output_count = 1
        inputs = [recipe_utils.get_item(current_recipe["template"]), recipe_utils.get_item(current_recipe["base"]), recipe_utils.get_item(current_recipe["addition"])]
    elif station == "smithing_transform":
        output_item = recipe_utils.get_item(current_recipe["result"])
        output_count = current_recipe["result"].get("count", 1)
        inputs = [recipe_utils.get_item(current_recipe["template"]), recipe_utils.get_item(current_recipe["base"]), recipe_utils.get_item(current_recipe["addition"])]
    elif (station == "campfire_cooking") or (station == "smoking") or (station == "blasting") or (station == "blasting_clear") or (station == "smelting") or (station == "smelting_clear"):
        experience = current_recipe.get("experience", "")
        cooking_time = current_recipe.get("cookingtime", "")
        output_item = current_recipe["result"].split(":")[1]
        output_count = 1
        inputs = [recipe_utils.get_ingredient(current_recipe["ingredient"])]
    else:
        print("Skipped recipe with name " + recipe_name)
        return

    num_spacers = 0

    if len(inputs) < 9:
        num_spacers = 9 - len(inputs)

    csv_writer.writerow([recipe_name, station, category, group,
                        experience, cooking_time, output_item, output_count] + inputs + num_spacers * [""])
    return


with open(path.join(source_recipes_dir, name + ".csv"), "w") as csv:
    csv_writer = writer(csv)
    csv_writer.writerow(header)

    for recipe in Path(vanilla_recipes_dir).glob("*.json"):
        with open(recipe) as loaded_recipe:
            recipe_to_csv(csv_writer, path.splitext(
                path.basename(recipe))[0], loaded_recipe)

    # for recipe in Path(custom_recipes_dir).glob("*.json"):
    #     with open(recipe) as loaded_recipe:
    #         recipe_to_csv(csv_writer, path.splitext(
    #             path.basename(recipe))[0], loaded_recipe)
