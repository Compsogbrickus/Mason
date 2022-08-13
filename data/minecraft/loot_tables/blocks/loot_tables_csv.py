import json
from pathlib import Path
from os import path
from csv import writer

import loot_table_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))
dir = script.parent.absolute()

loot_tables_folder = Path(dir).glob("*.json")

header = ["Base Block", "Block", "Count"]

with open(path.join(dir, "loot_tables_extracted.csv"), "w") as loot_tables_csv:
    loot_table_writer = writer(loot_tables_csv)
    loot_table_writer.writerow(header)

    for loot_table in loot_tables_folder:
        with open(loot_table) as loaded_loot_table:
            current_loot_table = json.load(loaded_loot_table)
            base_block, json_ext = path.splitext(path.basename(loot_table))
            block, count = "special", ""
            
            if len(current_loot_table.get("pools", [])) == 1:   
                loot_table_entries = current_loot_table["pools"][0]["entries"]

                if len(loot_table_entries) == 0:
                    block = ""
                elif len(loot_table_entries) == 1:
                    if loot_table_entries[0]["type"] == "minecraft:alternatives":
                        loot_table_entries_children = loot_table_entries[0]["children"]

                        for alternatives in range(len(loot_table_entries_children)):
                            block, count = loot_table_utils.item_explosion(loot_table_entries_children[alternatives], loot_table_entries_children[alternatives])
                    else:
                        block, count = loot_table_utils.item_explosion(loot_table_entries[0], current_loot_table["pools"][0])

            loot_table_writer.writerow([base_block, block, count])