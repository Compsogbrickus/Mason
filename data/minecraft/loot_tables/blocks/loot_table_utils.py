def blocks_empty ():

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

def blocks (base_block, block, count):

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