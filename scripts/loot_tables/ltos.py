# Copyright 2023 Compsogbrickus
# SPDX-License-Identifier: Apache-2.0

import json
from pathlib import Path
from os import path

import loot_table_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))

mason_dir = script.parents[2].absolute()
block_loot_tables_dir = path.join(mason_dir, "data/minecraft/loot_tables/blocks")

for loot_table in Path(block_loot_tables_dir).glob("*.json"):
    with open(loot_table, "r+") as loaded_loot_table:
        current_loot_table = json.load(loaded_loot_table)        
        base_block = path.splitext(path.basename(loot_table))[0]

        ltos = False
        if len(current_loot_table["pools"]) > 0:
            for pool in current_loot_table["pools"]:
                if len(pool["entries"]) > 0:
                    if pool["entries"][0].get("name", "") == "ltos:data":
                        ltos = True
        
        if not ltos:
            current_loot_table["pools"].append(loot_table_utils.ltos(base_block))

        loaded_loot_table.seek(0)

        json_structure = json.dumps(current_loot_table, indent=4)
        loaded_loot_table.write(json_structure)