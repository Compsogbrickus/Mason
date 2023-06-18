execute if score @s mason.opened.crafting_table matches 1.. run function mason:give/0_2
# execute if score @s mason.opened.crafting matches 1.. run function mason:give/1
# execute if score @s mason.opened.stonecutter matches 1.. run function mason:give/3
# execute if score @s mason.opened.smithing_table matches 1.. run function mason:give/4
# execute if score @s mason.opened.campfire matches 1.. run function mason:give/5
execute if score @s mason.opened.smoker matches 1.. run function mason:give/6
execute if score @s mason.opened.blast_furnace matches 1.. run function mason:give/7
execute if score @s mason.opened.furnace matches 1.. run function mason:give/8

execute if score @s mason.crafting_state matches 0.. run function mason:check_rotation