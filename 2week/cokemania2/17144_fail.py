def find_air_purifier(map_list):
    for i, m in enumerate(map_list):
        if m[0] == -1:
            return i, i + 1

def move_up(map_list, max_y, start_y, start_x):
    y = start_y
    x = start_x
    while y + 1 < max_y:
        if map_list[y][x] != -1:
            map_list[y][x] = map_list[y + 1][x]
        y += 1
    return y - 1, x

def move_left(map_list, max_x, start_y, start_x):
    y = start_y
    x = start_x
    while x + 1 < max_x:
        if map_list[y][x] != -1:
            map_list[y][x] = map_list[y][x + 1]
        x += 1
    return y, x - 1


def move_right(map_list, start_y, start_x):
    y = start_y
    x = start_x
    while x - 1 >= 0:
        if map_list[y][x] != -1:
            map_list[y][x - 1] = map_list[y][x]
        x -= 1
    return y, x + 1

def move_down(map_list, start_y, start_x):
    y = start_y
    x = start_x
    while y - 1 >= 0:
        if map_list[y][x] != -1:
            map_list[y - 1][x] = map_list[y][x]
        y -= 1
    return y + 1, x

def clock_direction(map_list, lower):
    max_y = len(map_list)
    max_x = len(map_list[0])

    start_y = lower
    start_x = 0

    start_y, start_x = move_up(map_list, max_y, start_y, start_x)
    start_y, start_x = move_left(map_list, max_x, start_y, start_x)
    start_y, start_x = move_down(map_list, start_y, start_x)
    move_right(map_list, start_y, start_x) 


def reversed_clock_direction(map_list, upper):
    max_y = len(map_list)
    max_x = len(map_list[0])

    start_y = upper
    start_x = 0

    start_y, start_x = move_down(map_list, start_y, start_x)
    start_y, start_x = move_left(map_list, max_x, start_y, start_x)
    start_y, start_x = move_up(map_list, max_y, start_y, start_x)
    move_right(map_list, start_y, start_x)

def spread_dust(map_list):
    ...

def air_purifier(map_list, upper, lower):
    reversed_clock_direction(map_list, upper)
    clock_direction(map_list, lower)

R, C, T = map(int, input().split())
map_list = []
for i in range(R):
    map_list.append(list(map(int, input().split())))

upper, lower = find_air_purifier(map_list)
for i in range(T):
    # spread_dust(map_list)
    air_purifier(map_list, upper, lower)


for m in map_list:
    print(m)

answer = sum([sum([x for x in y  if x != -1 ]) for y in map_list])
print(answer)
        