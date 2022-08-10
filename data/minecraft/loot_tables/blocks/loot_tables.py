import json
from pathlib import Path
from os import path
from csv import reader

script = Path(__file__)
name, ext = path.splitext(path.basename(script))
dir = script.parent.absolute()

with open(path.join(dir, name + ".csv"), newline="") as csv:
    csv_reader = reader(csv)
    header = next(csv_reader)
    for row in csv_reader:
        if row[1] == "air":
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
        else:
            structure = {
                "type": "minecraft:block",
                "pools": [
                    {
                        "bonus_rolls": 0.0,
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
                                        "name": "minecraft:" + row[0],
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
                                        "name": "minecraft:" + row[1],
                                        "functions": [
                                            {
                                                "function": "minecraft:set_count",
                                                "count": int(row[2])
                                            }
                                        ]
                                    }
                                ]
                            }
                        ],
                        "rolls": 1.0
                    }
                ]
            }

        json_structure = json.dumps(structure, indent=4)

        with open(path.join(dir, row[0] + ".json"), "w") as file_out:
            file_out.write(json_structure)
