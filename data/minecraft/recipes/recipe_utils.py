def stonecutting(base_block, block, count):

    structure = {
        "type": "minecraft:stonecutting",
        "count": count,
        "ingredient": {
            "item": "minecraft:" + base_block
        },
        "result": "minecraft:" + block
    }

    return (structure)
