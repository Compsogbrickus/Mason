# Simple Blocks

Simple Blocks is a datapack for Minecraft 1.19.4 that aims to reduce inventory clutter by simplifying block drops and recipes.

This repository functions as a datapack that can be dropped into a Minecraft world's "datapacks" folder. Once placed into the datapacks folder and once the world is reloaded, it will replace all vanilla block drops and recipes.

## Documentation

This datapack uses scripts written in Python paired with spreadsheets in CSV format to generate almost all the data files needed to replace vanilla block drops and recipes.

The source spreadsheets with usage notes are provided on Google Sheets at https://docs.google.com/spreadsheets/d/1e1b9jBrNWyr_0TeIGuodv0pg3ZAfBQGJ3JTmPyZcpbY/edit?usp=sharing. You can edit these for personal use via "File > Make a copy." Each tab can be downloaded in CSV format via "File > Download > Comma Separated Values (.csv)."

To report a bug or suggest a feature, use the Issues tracker on Github. Issues are forwarded to my email. For more detailed questions, you can reach me at compsogbrickus@gmail.com or on Discord as compsogbrickus.

### Block Drops

To read block drops from `data/minecraft/loot_tables/blocks` and store them as `sources/loot_tables/blocks_to_csv.csv`, run `scripts/loot_tables/blocks_to_csv.py`.

To overwrite `data/minecraft/loot_tables/blocks` with block drops from `sources/loot_tables/blocks.csv`, run `scripts/loot_tables/blocks.py`.

This datapack is designed to support **Loot Table Output Specification (aka ltos)** by gibbsly (https://github.com/gibbsly/ltos). Support is not enabled by default. To add support to all block drops currently in `data/minecraft/loot_tables/blocks`, run `scripts/loot_tables/ltos.py`.

### Recipes

To read recipes from `data/minecraft/recipes` and `data/simple_blocks/recipes` and store them as `sources/recipes/recipes_to_csv.csv`, run `scripts/recipes/recipes_to_csv.py`.

To overwrite `data/simple_blocks/recipes` with recipes from `sources/recipes/recipes.csv`, run `scripts/recipes/recipes.py`.

## Credits

**Compsogbrickus** - Datapack Creator. I wrote pretty much everything here!

**Misode** - Recipe and Block Drop structure templates. It would have been much, much more difficult to create standardized templates without the tools at https://misode.github.io/.

**Asometric** - Inspiration! This datapack was originally built to extend a handwritten collection of block loot tables created for the map Crimson Bay's Treasure. You can check out his work at https://www.crowdford.com/.

**Additional Credits** - Gibbsly, for putting up with my confusion over ltos.