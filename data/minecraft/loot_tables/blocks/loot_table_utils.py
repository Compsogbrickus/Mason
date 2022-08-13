def item_explosion(type_entry, conditions_entry):
    block = "special"
    count = ""

    if (type_entry["type"] == "minecraft:item") and (conditions_entry.get("conditions") == [{"condition": "minecraft:survives_explosion"}]):
        block = type_entry["name"].split(":")[1]
        function = type_entry.get("functions", "other")

        if function != "other":
            count = function[0].get("count", "special")
        else:
            count = 1
    return (block, count)


def blocks_empty():

    structure = {
        "type": "minecraft:block",
        "pools": [
            {
                "rolls": 1,
                "bonus_rolls": 0,
                "entries": []
            }
        ]
    }

    return (structure)


def blocks(base_block, block, count):

    structure = {
        "type": "minecraft:block",
        "pools": [
            {
                "rolls": 1,
                "bonus_rolls": 0,
                "entries": [
                    {
                        "type": "minecraft:alternatives",
                        "children": [
                            {
                                "type": "minecraft:item",
                                "conditions": [
                                    {
                                        "condition": "minecraft:match_tool",
                                        "predicate": {
                                            "enchantments": [
                                                {
                                                    "enchantment": "minecraft:silk_touch",
                                                    "levels": {
                                                        "min": 1
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                ],
                                "name": "minecraft:" + base_block,
                                "functions": [
                                    {
                                        "function": "minecraft:set_count",
                                        "count": 1
                                    }
                                ]
                            },
                            {
                                "type": "minecraft:item",
                                "conditions": [
                                    {
                                        "condition": "minecraft:survives_explosion"
                                    }
                                ],
                                "name": "minecraft:" + block,
                                "functions": [
                                    {
                                        "function": "minecraft:set_count",
                                        "count": count
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    return (structure)
