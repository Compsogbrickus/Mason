import json
from pathlib import Path
from os import path
from csv import writer

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
            loot_table_entries = current_loot_table["pools"][0]["entries"]

            base_block, json_ext = path.splitext(path.basename(loot_table))

            if loot_table_entries == []:
                block = ""
                count = ""
            else:
                block = loot_table_entries[0]["children"][1]["name"].split(":")[1]
                count = loot_table_entries[0]["children"][1]["functions"][0]["count"]

            loot_table_writer.writerow([base_block, block, count])