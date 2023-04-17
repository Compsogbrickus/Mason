execute if score @s simple_blocks.opened_crafting_table matches 1.. run function simple_blocks:grant_all
scoreboard players reset @s simple_blocks.opened_crafting_table

execute if score @s simple_blocks.using_crafting_table matches 1.. run execute summon marker run function simple_blocks:check_rotation
