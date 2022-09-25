import ast
import re

import unicodedata

def get_item(to_check):
    item_or_tag = to_check.get("item", "tag")

    if item_or_tag == "tag":
        item_or_tag = "#" + to_check["tag"].split(":")[1]
    else:
        item_or_tag = item_or_tag.split(":")[1]

    return (item_or_tag)


def get_ingredient(current_recipe_ingredient):
    inputs = []

    if isinstance(current_recipe_ingredient, list):
        for ingredients in current_recipe_ingredient:
            inputs.append(get_item(ingredients))
    else:
        inputs.append(get_item(current_recipe_ingredient))

    return (inputs)


def expand_item(item):

    if re.search("^\[", str(item)):
        item = ast.literal_eval(str(item))

    if isinstance(item, list):
        for entry in range(len(item)):
            item[entry] = expand_item(item[entry])
    else:
        if re.search("^\#", item):
            return ({"tag": "minecraft:" + re.sub("^\#", "", item)})
        else:
            return ({"item": "minecraft:" + item})

    return (item)


def advancement_void():

    structure = {
        "criteria": {
            "impossible": {
                "trigger": "minecraft:impossible"
            }
        }
    }

    return (structure)


def advancement_impossible_child_recipe(parent, recipe):

    structure = {
        "parent": parent,
        "criteria": {
            "impossible": {
                "trigger": "minecraft:impossible"
            }
        },
        "rewards": {
            "recipes": [
                recipe
            ]
        }
    }

    return (structure)


def spacing_check(pattern):

    entered_pattern = pattern.copy()

    height = len(pattern)
    width = len(pattern[0])

    # N S E W
    if pattern[0] == " "*width:
        del pattern[0]
        height -= 1
    if pattern[-1] == " "*width:
        del pattern[-1]
        height -= 1
    all_spaces_E = True
    all_spaces_W = True
    for index in range(height):
        if pattern[index][-1] != " ":
            all_spaces_E = False
        if pattern[index][0] != " ":
            all_spaces_W = False
    if all_spaces_E == True:
        for index in range(height):
            pattern[index] = pattern[index][:width-1]
        width -= 1
    if all_spaces_W == True:
        for index in range(height):
            pattern[index] = pattern[index][1:]
        width -= 1

    if pattern != entered_pattern:
        pattern = spacing_check(pattern)

    return (pattern)


def crafting_shaped(group, output_item, output_count, input_items):

    keys = ["C", "O", "M", "P", "S", "G", "B", "R", "K"]
    values = list(filter(lambda x: x != "", sorted(set(input_items))))

    for slot in range(len(input_items)):
        if input_items[slot] == "":
            input_items[slot] = " "
        else:
            for value in range(len(values)):
                if input_items[slot] == values[value]:
                    input_items[slot] = keys[value]

    pattern_rows = []

    for groups in range(int(len(input_items)/3)):
        pattern_row = input_items[int(
            3*groups)] + input_items[int(3*groups + 1)] + input_items[int(3*groups + 2)]
        pattern_rows.append(pattern_row)

    pattern_rows = spacing_check(pattern_rows)

    key_list = []

    for value in range(len(values)):
        key_list.append((keys[value], expand_item(values[value])))

    key_dict = dict(key_list)

    if group == "":
        structure = {
            "type": "minecraft:crafting_shaped",
            "pattern": pattern_rows,
            "key": key_dict,
            "result": {
                "item": "minecraft:" + output_item,
                "count": output_count
            }
        }
    else:
        structure = {
            "type": "minecraft:crafting_shaped",
            "group": group,
            "pattern": pattern_rows,
            "key": key_dict,
            "result": {
                "item": "minecraft:" + output_item,
                "count": output_count
            }
        }

    return (structure)


def crafting_shapeless(group, output_item, output_count, input_items):

    input_items = list(filter(None, input_items))

    if group == "":
        structure = {
            "type": "minecraft:crafting_shapeless",
            "ingredients": list(expand_item(input_items)),
            "result": {
                "item": "minecraft:" + output_item,
                "count": output_count
            }
        }
    else:
        structure = {
            "type": "minecraft:crafting_shapeless",
            "group": group,
            "ingredients": list(expand_item(input_items)),
            "result": {
                "item": "minecraft:" + output_item,
                "count": output_count
            }
        }

    return (structure)


def stonecutting(group, output_item, output_count, input_item):

    if group == "":
        structure = {
            "type": "minecraft:stonecutting",
            "count": output_count,
            "ingredient": expand_item(input_item),
            "result": "minecraft:" + output_item
        }
    else:
        structure = {
            "type": "minecraft:stonecutting",
            "group": group,
            "count": output_count,
            "ingredient": expand_item(input_item),
            "result": "minecraft:" + output_item
        }

    return (structure)


def smithing(group, result, result_count, base, addition):

    if group == "":
        structure = {
            "type": "minecraft:smithing",
            "base": expand_item(base),
            "addition": expand_item(addition),
            "result": {
                "item": "minecraft:" + result,
                "count": result_count
            }
        }
    else:
        structure = {
            "type": "minecraft:smithing",
            "group": group,
            "base": expand_item(base),
            "addition": expand_item(addition),
            "result": {
                "item": "minecraft:" + result,
                "count": result_count
            }
        }

    return (structure)


def cooking(station, group, experience, cooking_time, output_item, input_items):

    input_items = list(filter(None, input_items))

    if group == "":
        structure = {
            "type": "minecraft:" + station,
            "ingredient": expand_item(input_items),
            "result": "minecraft:" + output_item,
            "experience": experience,
            "cookingtime": cooking_time
        }
    else:
        structure = {
            "type": "minecraft:" + station,
            "group": group,
            "ingredient": expand_item(input_items),
            "result": "minecraft:" + output_item,
            "experience": experience,
            "cookingtime": cooking_time
        }

    return (structure)
