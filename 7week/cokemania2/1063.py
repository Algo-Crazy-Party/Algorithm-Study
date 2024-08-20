# https://www.acmicpc.net/problem/1063


def is_over_map(x, y):
    if x < ord('A') or x > ord('H') or y < 1 or y > 8:
        return True
    return False

def move_king_and_stone(king, stone, next_step):
    x, y = move_dict[next_step]
    next_x, next_y = ord(king[0]) + x, int(king[1]) + y
    stone_x, stone_y = ord(stone[0]), int(stone[1])
    next_stone_x, next_stone_y = stone_x + x, stone_y + y

    if is_over_map(next_x, next_y):
        return  king, stone
    if next_x == stone_x and next_y == stone_y:
        if is_over_map(next_stone_x, next_stone_y):
            return king, stone
        return chr(next_x) + str(next_y), chr(next_stone_x) + str(next_stone_y)
    return chr(next_x) + str(next_y), stone


king, stone, n = input().split()

# x, y
move_dict = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1 , -1),
    "LB": (-1, -1),
}

for i in range(int(n)):
    next_step = input()
    king, stone = move_king_and_stone(king, stone, next_step)

print(king)
print(stone)