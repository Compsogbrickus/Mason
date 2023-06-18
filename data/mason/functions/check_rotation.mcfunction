summon marker ~ ~ ~ {UUID:[I;1413624527,1948467303,-1080809217,1852075490]}
tp 544232cf-7423-4067-bf94-28ff6e646de2 @s

execute store result score 544232cf-7423-4067-bf94-28ff6e646de2 mason.yaw run data get entity 544232cf-7423-4067-bf94-28ff6e646de2 Rotation[0] 10
execute store result score 544232cf-7423-4067-bf94-28ff6e646de2 mason.pitch run data get entity 544232cf-7423-4067-bf94-28ff6e646de2 Rotation[1] 10

execute unless score @s mason.yaw matches -1800..1800 run scoreboard players operation @s mason.yaw = 544232cf-7423-4067-bf94-28ff6e646de2 mason.yaw
execute unless score @s mason.pitch matches -900..900 run scoreboard players operation @s mason.pitch = 544232cf-7423-4067-bf94-28ff6e646de2 mason.pitch

execute unless score @s mason.yaw = 544232cf-7423-4067-bf94-28ff6e646de2 mason.yaw run function mason:take
execute unless score @s mason.crafting_state matches ..-1 unless score @s mason.pitch = 544232cf-7423-4067-bf94-28ff6e646de2 mason.pitch run function mason:take

kill 544232cf-7423-4067-bf94-28ff6e646de2