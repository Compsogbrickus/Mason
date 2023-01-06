import json
from pathlib import Path
from os import path
from csv import writer

import loot_table_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))

simple_blocks_dir = script.parents[2].absolute()
block_loot_tables_dir = path.join(simple_blocks_dir, "data/minecraft/loot_tables/blocks")

for loot_table in Path(block_loot_tables_dir).glob("*.json"):
    with open(loot_table, "r+") as loaded_loot_table:
        current_loot_table = json.load(loaded_loot_table)
        
        base_block = path.splitext(path.basename(loot_table))[0]
        current_loot_table["pools"].append(loot_table_utils.ltos(base_block))

        loaded_loot_table.seek(0)

        json_structure = json.dumps(current_loot_table, indent=4)
        loaded_loot_table.write(json_structure)