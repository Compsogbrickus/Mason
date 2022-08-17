import json
from pathlib import Path
from os import path
from csv import reader

import loot_table_utils

script = Path(__file__)
name, ext = path.splitext(path.basename(script))
dir = script.parent.absolute()

with open(path.join(dir, name + ".csv"), newline="") as csv:
    csv_reader = reader(csv)
    header = next(csv_reader)
    # Header has Type, Base Block, Block, Count, Block, Count

    for row in csv_reader:
        type = row[0]
        base_block = row[1]
        block_1 = row[2]
        count_1 = row[3]
        block_2 = row[4]
        count_2 = row[5]

        if (type == "custom") or (type == "review"):
            continue
        elif type == "void":
            structure = loot_table_utils.blocks_void()
        elif type == "normal_0":
            structure = loot_table_utils.blocks_normal_0(base_block, int(count_1))
        elif type == "normal_1":
            structure = loot_table_utils.blocks_normal_1(block_1, int(count_1))
        elif type == "normal_2":
            structure = loot_table_utils.blocks_normal_2(block_1, int(count_1), block_2, int(count_2))
        elif type == "silk_0":
            structure = loot_table_utils.blocks_silk_0(base_block, int(count_1))
        elif type == "silk_1":
            structure = loot_table_utils.blocks_silk_1(base_block, block_1, int(count_1))
        elif type == "silk_2":
            structure = loot_table_utils.blocks_silk_2(base_block, block_1, int(count_1), block_2, int(count_2))
        elif type == "shears_0":
            structure = loot_table_utils.blocks_shears_0(base_block, int(count_1))
        elif type == "shears_1":
            structure = loot_table_utils.blocks_shears_1(base_block, block_1, int(count_1))
        elif type == "shears_2":
            structure = loot_table_utils.blocks_shears_2(base_block, block_1, int(count_1), block_2, int(count_2))
        elif type == "slab_0":
            structure = loot_table_utils.blocks_slab_0(base_block)
        elif type == "slab_1":
            structure = loot_table_utils.blocks_slab_1(base_block, block_1)
        elif type == "slab_2":
            structure = loot_table_utils.blocks_slab_2(base_block, block_1, block_2)
        else:
            print("Skipping block loot table with base block " + base_block + ".")

        json_structure = json.dumps(structure, indent=4)

        with open(path.join(dir, base_block + ".json"), "w") as file_out:
            file_out.write(json_structure)