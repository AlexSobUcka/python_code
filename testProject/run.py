"""
Если я вышел из дома в 6:52 утра и пробежал 1 км в легком темпе
(1 км за 8 мин. 15 сек.), потом 3 км в среднем темпе (1 км за 7 мин.
12 сек.) и 1 км в легком темпе снова, то во сколько я вернусь домой
позавтракать?
"""

start_time = 6 * 60 * 60 + 52 * 60
distance_light = 2000
light_temp = 1000 / (8 * 60 + 15) #скорость м/с
distance_medium = 3000
medium_temp = 1000 / (7 * 60 + 12) #скорость м/с

run_time = distance_medium / medium_temp + distance_light / light_temp
end_time_hour = str(int((start_time + run_time) // (60 * 60)))
end_time_minutes = str(int((start_time + run_time) // (60) - ((start_time + run_time) // (60 * 60)) * 60))
print(end_time_hour + ':' + end_time_minutes)
