# execute if score @s mason.crafting_state matches 0 run function mason:take/crafting
execute if score @s mason.crafting_state matches 1 run function mason:take/crafting_table
# execute if score @s mason.crafting_state matches 2 run function mason:take/stonecutter
# execute if score @s mason.crafting_state matches 3 run function mason:take/smithing_table
# execute if score @s mason.crafting_state matches 4 run function mason:take/campfire
execute if score @s mason.crafting_state matches 5 run function mason:take/smoker
execute if score @s mason.crafting_state matches 6 run function mason:take/blast_furnace
execute if score @s mason.crafting_state matches 7 run function mason:take/furnace

scoreboard players set @s mason.crafting_state -1
scoreboard players reset @s mason.pitch
scoreboard players reset @s mason.yaw