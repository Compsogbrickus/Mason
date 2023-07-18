# Crafting ids are 0 through 7 in this order:

# execute if score @s mason.opened.crafting matches 1.. run function mason:give/crafting
execute if score @s mason.opened.crafting_table matches 1.. run function mason:give/crafting_table
# execute if score @s mason.opened.stonecutter matches 1.. run function mason:give/stonecutter
# execute if score @s mason.opened.smithing_table matches 1.. run function mason:give/smithing_table
# execute if score @s mason.opened.campfire matches 1.. run function mason:give/campfire
execute if score @s mason.opened.smoker matches 1.. run function mason:give/smoker
execute if score @s mason.opened.blast_furnace matches 1.. run function mason:give/blast_furnace
execute if score @s mason.opened.furnace matches 1.. run function mason:give/furnace

execute if score @s mason.crafting_state matches 0.. run function mason:check_rotation