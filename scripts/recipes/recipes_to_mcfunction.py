# Copyright 2023 Compsogbrickus
# SPDX-License-Identifier: Apache-2.0

import json
from pathlib import Path
from os import path, makedirs
from shutil import rmtree
from contextlib import ExitStack

script = Path(__file__)
name, ext = path.splitext(path.basename(script))

mason_dir = script.parents[2].absolute()
vanilla_recipes_dir = path.join(mason_dir, "data/minecraft/recipes")
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

for dir in [give_recipes_dir, take_recipes_dir]:
    if path.exists(dir):
        rmtree(dir)
    makedirs(dir)

with ExitStack() as stack:
    give_recipes = [stack.enter_context(open(path.join(give_recipes_dir, fname + ".mcfunction"), "w")) for fname in recipe_types]
    take_recipes = [stack.enter_context(open(path.join(take_recipes_dir, fname + ".mcfunction"), "w")) for fname in recipe_types]

    for recipe in Path(vanilla_recipes_dir).glob("*.json"):
        with open(recipe) as loaded_recipe:
            filename = path.splitext(path.basename(recipe))[0]
            current_recipe = json.load(loaded_recipe)

            station = current_recipe["type"].split(":")[1]

            if station == "crafting_shaped":
                id = 0

                height = len(current_recipe["pattern"])

                if height > 2:
                    id = 1
                else:
                    for line in range(height):
                        if len(current_recipe["pattern"][line]) > 2:
                            id = 1
            elif station == "crafting_shapeless":
                if len(current_recipe["ingredients"]) < 5:
                    id = 2
                else:
                    id = 3
            elif station == "stonecutting":
                id = 4
            elif station == "smithing_transform":
                id = 5
            elif station == "smithing_trim":
                id = 6
            elif station == "campfire_cooking":
                id = 7
            elif station == "smoking":
                id = 8
            elif station == "blasting":
                id = 9
            elif station == "smelting":
                id = 10
            else:
                id = -1

                print("Adding recipe with no type " + filename)
            
            give_recipes[id].write("recipe give @s minecraft:" + filename + "\n")
            take_recipes[id].write("recipe take @s minecraft:" + filename + "\n")