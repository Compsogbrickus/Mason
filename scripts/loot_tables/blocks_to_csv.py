import json
from pathlib import Path
from os import path
from csv import writer

import loot_table_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))

simple_blocks_dir = script.parents[2].absolute()
block_loot_tables_dir = path.join(simple_blocks_dir, "data/minecraft/loot_tables/blocks")
source_loot_tables_dir = path.join(simple_blocks_dir, "sources/loot_tables")

header = ["Type", "Base Block", "Block", "Count", "Block", "Count"]

with open(path.join(source_loot_tables_dir, name + ".csv"), "w") as csv:
    csv_writer = writer(csv)
    csv_writer.writerow(header)

    for loot_table in Path(block_loot_tables_dir).glob("*.json"):
        with open(loot_table) as loaded_loot_table:
            current_loot_table = json.load(loaded_loot_table)
            table_type = "void" if current_loot_table == loot_table_utils.blocks_void() else "custom"
            base_block = path.splitext(path.basename(loot_table))[0]
            block_1, count_1 = "", ""
            block_2, count_2 = "", ""
            
            if table_type != "void":
                pools_count = len(current_loot_table["pools"])
                
                if pools_count == 1:
                    conditions = current_loot_table["pools"][0].get("conditions", "")

                    if conditions == [{'condition': 'minecraft:survives_explosion'}]:
                        name = current_loot_table["pools"][0]["entries"][0]["name"].split(":")[1]
                        count_1 = current_loot_table["pools"][0]["entries"][0]["functions"][0]["count"]

                        if name == base_block:
                            table_type = "blocks_normal_0"
                        else:
                            table_type = "blocks_normal_1"
                            block_1 = name
                    elif conditions == [{'condition': 'minecraft:match_tool', 'predicate': {'enchantments': [{'enchantment': 'minecraft:silk_touch', 'levels': {'min': 1}}]}}]:
                        functions = current_loot_table["pools"][0]["entries"][0].get("functions", "")
                        
                        if len(functions) == 1:
                            count_1 = functions[0]["count"]

                            if functions[0].get("conditions", "") == "":
                                table_type = "blocks_silk_0"
                            else:
                                table_type = "blocks_slab_0"
                    else:
                        entry = current_loot_table["pools"][0]["entries"][0]
                        
                        if entry["type"] == "minecraft:alternatives":
                            child_count = len(entry["children"])

                            if child_count == 2:
                                conditions = entry["children"][0].get("conditions", "")

                                if conditions == [{'condition': 'minecraft:match_tool', 'predicate': {'items': ['minecraft:shears']}}]:
                                    table_type = "blocks_shears_0"
                                    count_1 = entry["children"][0]["functions"][0]["count"]
                                    
                                    if not isinstance(count_1, int):
                                        table_type = "custom"
                                elif entry["children"][1]["type"] == "minecraft:group":
                                    block_1 = entry["children"][1]["children"][0]["name"].split(":")[1]
                                    block_2 = entry["children"][1]["children"][1]["name"].split(":")[1]
                                    functions_1 = entry["children"][1]["children"][0].get("functions", "")
                                    functions_2 = entry["children"][1]["children"][1].get("functions", "")

                                    if len(functions_1) == 1 and len(functions_2) == 1:
                                        count_1 = functions_1[0]["count"]
                                        count_2 = functions_2[0]["count"]

                                        if (functions_1[0].get("conditions", "") == "") and (functions_2[0].get("conditions", "") == ""):
                                            table_type = "blocks_silk_2"
                                        else:
                                            table_type = "blocks_slab_2"
                                else:
                                    second_child = entry["children"][1]
                                    block_1 = second_child["name"].split(":")[1]
                                    functions = second_child.get("functions", "")

                                    if len(functions) == 1:
                                        count_1 = functions[0]["count"]

                                        if functions[0].get("conditions", "") == "":
                                            table_type = "blocks_silk_1"
                                        else:
                                            table_type = "blocks_slab_1"
                            elif child_count == 3:
                                last_child_type = entry["children"][2]["type"]

                                if last_child_type == "minecraft:item":
                                    table_type = "blocks_shears_1"
                                    block_1 = entry["children"][2]["name"].split(":")[1]
                                    count_1 = entry["children"][2]["functions"][0]["count"]
                                elif last_child_type == "minecraft:group":
                                    if len(last_child_type["children"]) == 2:
                                        table_type = "blocks_shears_2"
                                        block_1 = last_child_type["children"][0]["name"].split(":")[1]
                                        count_1 = last_child_type["children"][0][0]["count"]
                                        block_2 = last_child_type["children"][1]["name"].split(":")[1]
                                        count_2 = last_child_type["children"][1][0]["count"]
                elif pools_count == 2:
                    block_1 = current_loot_table["pools"][0]["entries"][0]["name"].split(":")[1]
                    block_2 = current_loot_table["pools"][1]["entries"][0]["name"].split(":")[1]
                    functions_1 = current_loot_table["pools"][0]["entries"][0].get("functions", "")
                    functions_2 = current_loot_table["pools"][1]["entries"][0].get("functions", "")

                    if functions_1 != "" and functions_2 != "":
                        table_type = "blocks_normal_2"
                        count_1 = functions_1[0]["count"]
                        count_2 = functions_2[0]["count"]
                
            csv_writer.writerow([table_type, base_block, block_1, count_1, block_2, count_2])