from collections import deque

def _is_possible_z(z, max_z):
    return z >= 0 and z < max_z

def _is_possible_coordinate(x, y, max_x, max_y):
    return _is_possible_z(y, max_y) and _is_possible_z(x, max_x)

def _is_possible_map(x, y, map_list):
    return map_list[y][x] == 0

def _is_minumum_count(x, y, visited, count):
    return count < visited[y][x]

def is_possible_condition(max_x, max_y, n_list, visited, next_x, next_y, count):
    return _is_possible_coordinate(next_x, next_y, max_x, max_y) and _is_possible_map(next_x, next_y, n_list) and _is_minumum_count(next_x, next_y, visited, count)

def get_next_steps(x, y, horse_count, max_x, max_y, count, n_list, visited):
    monkey_steps_y = [1, 0, -1, 0]
    monkey_steps_x = [0, 1, 0, -1]

    horse_steps_y = [-1, -2, -2, -1, 1, 2, 2, 1]
    horse_steps_x = [-2, -1, 1, 2, 2, 1, -1, -2]

    steps = []
    for i in range(len(monkey_steps_y)):
        next_x = x + monkey_steps_x[i]
        next_y = y + monkey_steps_y[i]
        if is_possible_condition(max_x, max_y, n_list, visited, next_x, next_y, count):
            steps.append([next_y, next_x, count + 1, horse_count])
    
    if horse_count > 0:
        for i in range(len(horse_steps_y)):
            next_x = x + horse_steps_x[i]
            next_y = y + horse_steps_x[i]
            if is_possible_condition(max_x, max_y, n_list, visited, next_x, next_y, count):
                steps.append([next_y, next_x, count + 1, horse_count - 1])
    return steps

def set_next_steps(steps, visited):
    for step in steps:
        visited[step[0]][step[1]] = min(visited[step[0]][step[1]],step[2])

horse_count = int(input())
max_x, max_y = map(int, input().split())
n_list = []

visited = [[max_x * max_y for _ in range(max_x)] for _ in range(max_y)]

for i in range(max_y):
    n_list.append(list(map(int, input().split())))

# x, y , count, horse_count
nodes = deque([[0 , 0, 0, horse_count]])
while nodes:
    y, x, count, horse_count = nodes.popleft()
    if y == max_y - 1 and x == max_x -1:
        print(count)
        break
    steps = get_next_steps(x, y, horse_count, max_x, max_y, count, n_list, visited)
    print(steps)
    set_next_steps(steps, visited)
    for step in steps:
        nodes.append(step)


# 실패