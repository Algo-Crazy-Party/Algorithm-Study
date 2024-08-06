def can_make_target(s, t):
    while len(t) > len(s):
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] == 'B':
            t = t[:-1][::-1]
        else:
            return 0
    return 1 if s == t else 0

s = input()
t = input()

print(can_make_target(s, t))