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
    # Header has Type, Collection, Station, Group, Subdirectory, Experience, Cooking Time (Ticks), Output Item, Output Count, Input x9

    with open(path.join(functions_dir, "setup.mcfunction"), "w") as setup_function:
        setup_function.write(
            "gamerule doLimitedCrafting true\nadvancement grant @s from simple_blocks:recipes/root")

    for row in csv_reader:
        type = row[0]
        collection = row[1]
        station = row[2]
        group = row[3]
        subdir = row[4]
        experience = row[5]
        cooking_time = row[6]
        output_item = row[7]
        output_count = row[8]
        input_1, input_2, input_3 = row[9], row[10], row[11]
        input_4, input_5, input_6 = row[12], row[13], row[14]
        input_7, input_8, input_9 = row[15], row[16], row[17]

        experience = 0 if experience == "" else float(experience)
        cooking_time = 0 if cooking_time == "" else float(cooking_time)
        output_count = 0 if output_count == "" else int(output_count)

        if type == "custom":
            continue
        elif type == "normal":
            if station == "crafting_shaped":
                recipe_structure = recipe_utils.crafting_shaped(group, output_item, int(output_count), [input_1, input_2, input_3, input_4, input_5, input_6, input_7, input_8, input_9]) if type == "normal" else ""
                filename = output_item
            elif station == "crafting_shapeless":
                recipe_structure = recipe_utils.crafting_shapeless(group, output_item, int(output_count), [input_1, input_2, input_3, input_4, input_5, input_6, input_7, input_8, input_9]) if type == "normal" else ""
                filename = output_item
            elif station == "stonecutting":
                recipe_structure = recipe_utils.stonecutting(group, output_item, int(output_count), input_1) if type == "normal" else ""
                filename = output_item + "_from_" + input_1 + "_stonecutting"
            elif station == "smithing":
                recipe_structure = recipe_utils.smithing(group, output_item, output_count, input_1, input_2) if type == "normal" else ""
                filename = output_item + "_smithing"
            elif station == "campfire_cooking":
                recipe_structure = recipe_utils.cooking(station, group, experience, cooking_time, output_item, row[9:]) if type == "normal" else ""
                filename = output_item + "_from_campfire_cooking"
            elif station == "smoking":
                recipe_structure = recipe_utils.cooking(station, group, experience, cooking_time, output_item, row[9:]) if type == "normal" else ""
                filename = output_item + "_from_smoking"
            elif station == "blasting":
                recipe_structure = recipe_utils.cooking(station, group, experience, cooking_time, output_item, row[9:]) if type == "normal" else ""
                filename = output_item + "_from_blasting"
            elif station == "blasting_clear":
                recipe_structure = recipe_utils.cooking("blasting", group, experience, cooking_time, output_item, row[9:]) if type == "normal" else ""
                filename = output_item + "_from_blasting_" + input_1
            elif station == "smelting":
                recipe_structure = recipe_utils.cooking(station, group, experience, cooking_time, output_item, row[9:]) if type == "normal" else ""
                filename = output_item + "_from_smelting"
            elif station == "smelting_clear":
                recipe_structure = recipe_utils.cooking("smelting", group, experience, cooking_time, output_item, row[9:]) if type == "normal" else ""
                filename = output_item + "_from_smelting_" + input_1
            else:
                print("Skipping recipe with output item " + output_item + ".")
                continue

            
            if collection == "custom":
                recipes_dir = custom_recipes_dir
                advancements_dir = custom_advancements_dir
                advancement_structure = recipe_utils.advancement_impossible_child_recipe("simple_blocks:recipes/root", "simple_blocks:" + filename)
            else:
                print("Skipping recipe with output item " + output_item + ".")
                continue
                
            with open(path.join(recipes_dir, filename + ".json"), "w") as file_out:
                file_out.write(json.dumps(recipe_structure, indent=4))
        
            with open(path.join(advancements_dir, filename + ".json"), "w") as file_out:
                    file_out.write(json.dumps(advancement_structure, indent=4))
        else:
            print("Skipping recipe with output item " + output_item + ".")
            continue