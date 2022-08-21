
def blocks_void():

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


def blocks_normal_0(base_block, count):

    structure = {
        "type": "minecraft:block",
        "pools": [
            {
                "rolls": 1,
                "bonus_rolls": 0,
                "conditions": [
                    {
                        "condition": "minecraft:survives_explosion"
                    }
                ],
                "entries": [
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:" + base_block,
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

    return (structure)


def blocks_normal_1(block, count):

    structure = {
        "type": "minecraft:block",
        "pools": [
            {
                "rolls": 1,
                "bonus_rolls": 0,
                "conditions": [
                    {
                        "condition": "minecraft:survives_explosion"
                    }
                ],
                "entries": [
                    {
                        "type": "minecraft:item",
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

    return (structure)


def blocks_normal_2(block_1, count_1, block_2, count_2):

    structure = {
        "type": "minecraft:block",
        "pools": [
            {
                "rolls": 1,
                "bonus_rolls": 0,
                "entries": [
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:" + block_1,
                        "functions": [
                            {
                                "function": "minecraft:set_count",
                                "count": count_1
                            }
                        ]
                    }
                ]
            },
            {
                "rolls": 1,
                "bonus_rolls": 0,
                "entries": [
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:" + block_2,
                        "functions": [
                            {
                                "function": "minecraft:set_count",
                                "count": count_2
                            }
                        ]
                    }
                ]
            }
        ]
    }

    return (structure)


def blocks_silk_0(base_block, count):

    structure = {
        "type": "minecraft:block",
        "pools": [
            {
                "rolls": 1,
                "bonus_rolls": 0,
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
                "entries": [
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:" + base_block,
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

    return (structure)


def blocks_silk_1(base_block, block, count):

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


def blocks_silk_2(base_block, block_1, count_1, block_2, count_2):

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
                                "name": "minecraft:" + base_block,
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
                                ]
                            },
                            {
                                "type": "minecraft:group",
                                "children": [
                                    {
                                        "type": "minecraft:item",
                                        "name": "minecraft:" + block_1,
                                        "functions": [
                                            {
                                                "function": "minecraft:set_count",
                                                "count": count_1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "minecraft:item",
                                        "name": "minecraft:" + block_2,
                                        "functions": [
                                            {
                                                "function": "minecraft:set_count",
                                                "count": count_2
                                            }
                                        ]
                                    }
                                ],
                                "conditions": [
                                    {
                                        "condition": "minecraft:survives_explosion"
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


def blocks_shears_0(base_block, count):

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
                                "name": "minecraft:" + base_block,
                                "functions": [
                                    {
                                        "function": "minecraft:set_count",
                                        "count": count
                                    }
                                ],
                                "conditions": [
                                    {
                                        "condition": "minecraft:match_tool",
                                        "predicate": {
                                            "items": [
                                                "minecraft:shears"
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "minecraft:item",
                                "name": "minecraft:" + base_block,
                                "functions": [
                                    {
                                        "function": "minecraft:set_count",
                                        "count": count
                                    }
                                ],
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
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    return (structure)


def blocks_shears_1(base_block, block, count):

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
                                "name": "minecraft:" + base_block,
                                "conditions": [
                                    {
                                        "condition": "minecraft:match_tool",
                                        "predicate": {
                                            "items": [
                                                "minecraft:shears"
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "minecraft:item",
                                "name": "minecraft:" + base_block,
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
                                ]
                            },
                            {
                                "type": "minecraft:item",
                                "name": "minecraft:" + block,
                                "functions": [
                                    {
                                        "function": "minecraft:set_count",
                                        "count": count
                                    }
                                ],
                                "conditions": [
                                    {
                                        "condition": "minecraft:survives_explosion"
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


def blocks_shears_2(base_block, block_1, count_1, block_2, count_2):

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
                                "name": "minecraft:" + base_block,
                                "conditions": [
                                    {
                                        "condition": "minecraft:match_tool",
                                        "predicate": {
                                            "items": [
                                                "minecraft:shears"
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "minecraft:item",
                                "name": "minecraft:" + base_block,
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
                                ]
                            },
                            {
                                "type": "minecraft:group",
                                "children": [
                                    {
                                        "type": "minecraft:item",
                                        "name": "minecraft:" + block_1,
                                        "functions": [
                                            {
                                                "function": "minecraft:set_count",
                                                "count": count_1
                                            }
                                        ]
                                    },
                                    {
                                        "type": "minecraft:item",
                                        "name": "minecraft:" + block_2,
                                        "functions": [
                                            {
                                                "function": "minecraft:set_count",
                                                "count": count_2
                                            }
                                        ]
                                    }
                                ],
                                "conditions": [
                                    {
                                        "condition": "minecraft:survives_explosion"
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


def blocks_slab_0(base_block):

    structure = {
        "type": "minecraft:block",
        "pools": [
            {
                "rolls": 1,
                "bonus_rolls": 0,
                "entries": [
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:" + base_block,
                        "functions": [
                            {
                                "function": "minecraft:set_count",
                                "count": 2,
                                "add": False,
                                "conditions": [
                                    {
                                        "condition": "minecraft:block_state_property",
                                        "block": "minecraft:" + base_block,
                                        "properties": {
                                            "type": "double"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ],
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
                ]
            }
        ]
    }

    return (structure)


def blocks_slab_1(base_block, block):

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
                                "name": "minecraft:" + base_block,
                                "functions": [
                                    {
                                        "function": "minecraft:set_count",
                                        "count": 2,
                                        "add": False,
                                        "conditions": [
                                            {
                                                "condition": "minecraft:block_state_property",
                                                "block": "minecraft:stone_slab",
                                                "properties": {
                                                    "type": "double"
                                                }
                                            }
                                        ]
                                    }
                                ],
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
                                ]
                            },
                            {
                                "type": "minecraft:item",
                                "name": "minecraft:" + block,
                                "functions": [
                                    {
                                        "function": "minecraft:set_count",
                                        "count": 2,
                                        "add": False,
                                        "conditions": [
                                            {
                                                "condition": "minecraft:block_state_property",
                                                "block": "minecraft:blackstone_slab",
                                                "properties": {
                                                    "type": "double"
                                                }
                                            }
                                        ]
                                    }
                                ],
                                "conditions": [
                                    {
                                        "condition": "minecraft:survives_explosion"
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


def blocks_slab_2(base_block, block_1, block_2):

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
                                "name": "minecraft:" + base_block,
                                "functions": [
                                    {
                                        "function": "minecraft:set_count",
                                        "count": 2,
                                        "add": False,
                                        "conditions": [
                                            {
                                                "condition": "minecraft:block_state_property",
                                                "block": "minecraft:" + base_block,
                                                "properties": {
                                                    "type": "double"
                                                }
                                            }
                                        ]
                                    }
                                ],
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
                                ]
                            },
                            {
                                "type": "minecraft:group",
                                "children": [
                                    {
                                        "type": "minecraft:item",
                                        "name": "minecraft:" + block_1,
                                        "functions": [
                                            {
                                                "function": "minecraft:set_count",
                                                "count": 2,
                                                "add": False,
                                                "conditions": [
                                                    {
                                                        "condition": "minecraft:block_state_property",
                                                        "block": "minecraft:" + base_block,
                                                        "properties": {
                                                            "type": "double"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "type": "minecraft:item",
                                        "name": "minecraft:" + block_2,
                                        "functions": [
                                            {
                                                "function": "minecraft:set_count",
                                                "count": 2,
                                                "add": False,
                                                "conditions": [
                                                    {
                                                        "condition": "minecraft:block_state_property",
                                                        "block": "minecraft:" + base_block,
                                                        "properties": {
                                                            "type": "double"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ],
                                "conditions": [
                                    {
                                        "condition": "minecraft:survives_explosion"
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
