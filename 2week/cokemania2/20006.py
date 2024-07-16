def is_matched(room, level, m):
    if is_matchable_level(room, level) and not is_full(room, m):
        return True

def is_matchable_level(room, level):
    bangjang_level = room[0][0]
    return level <= bangjang_level + 10 and level >= bangjang_level - 10

def is_full(room, m):
    return len(room) == m

def is_started(room, m):
    return is_full(room, m)

def print_room_boys(room):
    room.sort(key=lambda x: x[1])
    for boy in room:
        print(boy[0], boy[1])

p, m = map(int, input().split())
rooms = []
for i in range(p):
    level, nickname = input().split()
    level = int(level)
    for room in rooms:
        if is_matched(room, level, m):
            room.append([level, nickname])
            break
    else:
        rooms.append([[level, nickname]])
            
for room in rooms:
    if is_started(room, m):
        print("Started!")
    else:
        print("Waiting!")
    print_room_boys(room)