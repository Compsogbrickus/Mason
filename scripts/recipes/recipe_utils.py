def advancement_void():

    structure = {
        "criteria": {
            "impossible": {
                "trigger": "minecraft:impossible"
            }
        }
    }

    return (structure)


def stonecutting(output_block, output_count, input_block):

    structure = {
        "type": "minecraft:stonecutting",
        "count": output_count,
        "ingredient": {
            "item": "minecraft:" + input_block
        },
        "result": "minecraft:" + output_block
    }

    return (structure)
