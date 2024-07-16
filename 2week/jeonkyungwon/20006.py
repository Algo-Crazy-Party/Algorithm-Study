import sys
input = sys.stdin.readline

p, m = map(int, input().split())
players = []

for _ in range(p):
    l, n = input().split()
    players.append([int(l), n])

rooms = []

for player in players:
    level, name = player
    placed = False

    for room in rooms:
        if len(room) < m and abs(room[0][0] - level) <= 10:
            room.append(player)
            placed = True
            break

    if not placed:
        rooms.append([player])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    room.sort(key=lambda x: x[1])
    for player in room:
        print(player[0], player[1])