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
vanilla_advancements_dir = path.join(
    simple_blocks_dir, "data/minecraft/advancements/recipes")
functions_dir = path.join(simple_blocks_dir, "data/simple_blocks/functions")

with open(path.join(source_recipes_dir, name + ".csv"), newline="") as csv:
    csv_reader = reader(csv)
    header = next(csv_reader)
    # Header has Type, Collection, Station, Group, Experience, Cooking Time (Ticks), Output Item, Output Count, Input x9

    with open(path.join(functions_dir, "setup.mcfunction"), "w") as setup_function:
        setup_function.write(
            "gamerule doLimitedCrafting true\nadvancement grant @s from minecraft:recipes/root")

    for row in csv_reader:
        type = row[0]
        collection = row[1]
        station = row[2]
        group = row[3]
        experience = row[4]
        cooking_time = row[5]
        output_item = row[6]
        output_count = row[7]
        input_1, input_2, input_3 = row[8], row[9], row[10]
        input_4, input_5, input_6 = row[11], row[12], row[13]
        input_7, input_8, input_9 = row[14], row[15], row[16]

        if type == "custom":
            continue
        elif type == "void":
            structure = recipe_utils.advancement_void()

            if station == "crafting_shaped" or station == "crafting_shapeless" or station == "crafting_unknown":
                filename = output_item
            elif station == "stonecutting":
                filename = output_item + "_from_" + input_1 + "_stonecutting"
            elif station == "smithing":
                filename = output_item + "_smithing"
            elif station == "campfire_cooking":
                filename = output_item + "_from_campfire_cooking"
            elif station == "smoking":
                filename = output_item + "_from_smoking"
            elif station == "blasting":
                filename = output_item + "_from_blasting"
            elif station == "blasting_clear":
                filename = output_item + "_from_blasting_" + input_1
            elif station == "smelting":
                filename = output_item + "_from_smelting"
            elif station == "smelting_clear":
                filename = output_item + "_from_smelting_" + input_1
            else:
                print("Skipping voided recipe with output item " + output_item + ".")
                continue

            if collection == "vanilla":
                if group == "":
                    dir = vanilla_advancements_dir
                    with open(path.join(functions_dir, "setup.mcfunction"), "a") as setup_function:
                        setup_function.write(
                            "\nadvancement revoke @s only minecraft:recipes/" + filename)
                else:
                    dir = path.join(vanilla_advancements_dir, group)
                    with open(path.join(functions_dir, "setup.mcfunction"), "a") as setup_function:
                        setup_function.write(
                            "\nadvancement revoke @s only minecraft:recipes/" + group + "/" + filename)
            else:
                print("Skipping voided recipe with output item " + output_item + ".")
                continue
        elif type == "normal":
            if collection == "vanilla":
                dir = vanilla_recipes_dir
            elif collection == "custom":
                dir = custom_recipes_dir
            else:
                print("Skipping recipe with output item " + output_item + ".")
                continue

            if station == "crafting_shaped":
                structure = recipe_utils.crafting_shaped(group, output_item, int(output_count), [input_1, input_2, input_3, input_4, input_5, input_6, input_7, input_8, input_9])
                filename = output_item
            elif station == "crafting_shapeless":
                structure = recipe_utils.crafting_shapeless(group, output_item, int(output_count), [input_1, input_2, input_3, input_4, input_5, input_6, input_7, input_8, input_9])
                filename = output_item
            elif station == "stonecutting":
                structure = recipe_utils.stonecutting(group,
                    output_item, int(output_count), input_1)
                filename = output_item + "_from_" + input_1 + "_stonecutting"
            elif station == "smithing":
                structure = recipe_utils.smithing(group, output_item, output_count, input_1, input_2)
                filename = output_item + "_smithing"
            elif station == "campfire_cooking":
                structure = recipe_utils.cooking(station, group, experience, cooking_time, output_item, row[8:])
                filename = output_item + "_from_campfire_cooking"
            elif station == "smoking":
                structure = recipe_utils.cooking(station, group, experience, cooking_time, output_item, row[8:])
                filename = output_item + "_from_smoking"
            elif station == "blasting":
                structure = recipe_utils.cooking(station, group, experience, cooking_time, output_item, row[8:])
                filename = output_item + "_from_blasting"
            elif station == "blasting_clear":
                structure = recipe_utils.cooking(station, group, experience, cooking_time, output_item, row[8:])
                filename = output_item + "_from_blasting_" + input_1
            elif station == "smelting":
                structure = recipe_utils.cooking(station, group, experience, cooking_time, output_item, row[8:])
                filename = output_item + "_from_smelting"
            elif station == "smelting_clear":
                structure = recipe_utils.cooking(station, group, experience, cooking_time, output_item, row[8:])
                filename = output_item + "_from_smelting_" + input_1
            else:
                print("Skipping recipe with output item " + output_item + ".")
                continue
        else:
            print("Skipping recipe with output item " + output_item + ".")
            continue

        json_structure = json.dumps(structure, indent=4)

        with open(path.join(dir, filename + ".json"), "w") as file_out:
            file_out.write(json_structure)
