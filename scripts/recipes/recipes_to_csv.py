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
vanilla_advancements_dir = path.join(
    simple_blocks_dir, "data/minecraft/advancements/recipes")

header = ["Type", "Collection", "Station", "Group", "Subdirectory", "Experience",
          "Cooking Time (Ticks)", "Output Item", "Output Count", "Input", "Input", "Input", "Input", "Input", "Input", "Input", "Input", "Input"]


def advancement_to_csv(csv_writer, advancement_name, loaded_advancement):
    if json.load(loaded_advancement) != recipe_utils.advancement_void():
        return

    subdir = path.basename(advancement.parent.absolute())
    output_item = re.sub(
        "(_from.*)|(_smithing.*)|(\.json)", "", advancement_name)

    if re.search("(" + output_item + ".json)|(_from_honeycomb)", advancement_name):
        station = "crafting_unknown"
    elif re.search("_stonecutting", advancement_name):
        station = "stonecutting"
    elif re.search("_smithing", advancement_name):
        station = "smithing"
    elif re.search("_from_campfire_cooking", advancement_name):
        station = "campfire_cooking"
    elif re.search("_from_smoking", advancement_name):
        station = "smoking"
    elif re.search("_from_blasting\.json", advancement_name):
        station = "blasting"
    elif re.search("_from_blasting_", advancement_name):
        station = "blasting_clear"
    elif re.search("_from_smelting\.json", advancement_name):
        station = "smelting"
    elif re.search("_from_smelting_", advancement_name):
        station = "smelting_clear"
    else:
        print("Skipped void advancement with name " + advancement_name)
        return

    csv_writer.writerow(["void", "vanilla", station, "",
                        subdir, "", "", output_item])
    return


def recipe_to_csv(csv_writer, recipe_name, loaded_recipe, collection):
    current_recipe = json.load(loaded_recipe)

    station = current_recipe["type"].split(":")[1]

    if re.search("_from_blasting_", recipe_name):
        station = "blasting_clear"
    elif re.search("_from_smelting_", recipe_name):
        station = "smelting_clear"

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
                if isinstance(current_recipe["key"][key], list):
                    value = []

                    for sub_item in range(len(current_recipe["key"][key])):
                        value.append(recipe_utils.get_item(
                            current_recipe["key"][key][sub_item]))
                else:
                    value = recipe_utils.get_item(current_recipe["key"][key])

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
            inputs += recipe_utils.get_ingredient(
                current_recipe["ingredients"][ingredient])
    elif station == "stonecutting":
        output_item = current_recipe["result"].split(":")[1]
        output_count = current_recipe["count"]
        inputs = recipe_utils.get_ingredient(current_recipe["ingredient"])
    elif station == "smithing":
        output_item = recipe_utils.get_item(current_recipe["result"])
        output_count = current_recipe["result"].get("count", 1)
        inputs = [recipe_utils.get_item(
            current_recipe["base"]), recipe_utils.get_item(current_recipe["addition"])]
    elif (station == "campfire_cooking") or (station == "smoking") or (station == "blasting") or (station == "blasting_clear") or (station == "smelting") or (station == "smelting_clear"):
        experience = current_recipe.get("experience", "")
        cooking_time = current_recipe.get("cookingtime", "")
        output_item = current_recipe["result"].split(":")[1]
        output_count = 1
        inputs = recipe_utils.get_ingredient(current_recipe["ingredient"])
    else:
        print("Skipped recipe with name " + recipe_name)
        return

    csv_writer.writerow(["normal", collection, station, group, "",
                        experience, cooking_time, output_item, output_count] + inputs)
    return


with open(path.join(source_recipes_dir, name + ".csv"), "w") as csv:
    csv_writer = writer(csv)
    csv_writer.writerow(header)

    for sub_item in Path(vanilla_advancements_dir).glob("*"):
        if path.isdir(sub_item):
            for advancement in Path(sub_item).glob("*.json"):
                with open(advancement) as loaded_advancement:
                    advancement_to_csv(csv_writer, path.basename(
                        advancement), loaded_advancement)

    for recipe in Path(vanilla_recipes_dir).glob("*.json"):
        with open(recipe) as loaded_recipe:
            recipe_to_csv(csv_writer, path.splitext(
                path.basename(recipe))[0], loaded_recipe, "vanilla")

    for recipe in Path(custom_recipes_dir).glob("*.json"):
        with open(recipe) as loaded_recipe:
            recipe_to_csv(csv_writer, path.splitext(
                path.basename(recipe))[0], loaded_recipe, "custom")
