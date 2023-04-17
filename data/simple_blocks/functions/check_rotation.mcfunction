tp @s @p[scores={simple_blocks.using_crafting_table=1..}]

execute store result score @s simple_blocks.pitch run data get entity @s Rotation[0] 10
execute store result score @s simple_blocks.yaw run data get entity @s Rotation[1] 10

execute unless score @p[scores={simple_blocks.using_crafting_table=1..}] simple_blocks.pitch matches -1800..1800 run scoreboard players operation @p[scores={simple_blocks.using_crafting_table=1..}] simple_blocks.pitch = @s simple_blocks.pitch
execute unless score @p[scores={simple_blocks.using_crafting_table=1..}] simple_blocks.yaw matches -900..900 run scoreboard players operation @p[scores={simple_blocks.using_crafting_table=1..}] simple_blocks.yaw = @s simple_blocks.yaw

execute unless score @p[scores={simple_blocks.using_crafting_table=1..}] simple_blocks.pitch = @s simple_blocks.pitch run execute as @p[scores={simple_blocks.using_crafting_table=1..}] run function simple_blocks:revoke_all

kill @s