def count_time(floor_list, time_to_leave, num_leave):
    floor_to_up = int(floor_list[num_leave-1])
    min_floor = int(floor_list[0])
    max_floor = int(floor_list[-1])
    if floor_to_up < time_to_leave:
        time = max_floor - min_floor
    else:
        up_time = max_floor - floor_to_up
        down_time = floor_to_up - min_floor
        if up_time >= down_time:
            time = down_time + max_floor - min_floor
        else:
            time = up_time + max_floor - min_floor
    return time


n, t = list(map(int, input().split()))
floors = list(input().split())
num_leave = int(input())

time = count_time(floors, t, num_leave)
print(time)