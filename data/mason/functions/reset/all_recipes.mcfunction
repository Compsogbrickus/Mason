recipe take @s *

function mason:give/persistent
# execute if score @s mason.crafting_state matches 0 run function mason:give/crafting
execute if score @s mason.crafting_state matches 1 run function mason:give/crafting_table
# execute if score @s mason.crafting_state matches 2 run function mason:give/stonecutter
# execute if score @s mason.crafting_state matches 3 run function mason:give/smithing_table
# execute if score @s mason.crafting_state matches 4 run function mason:give/campfire
execute if score @s mason.crafting_state matches 5 run function mason:give/smoker
execute if score @s mason.crafting_state matches 6 run function mason:give/blast_furnace
execute if score @s mason.crafting_state matches 7 run function mason:give/furnace