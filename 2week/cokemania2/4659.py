def is_in_vowel(s):
    for c in s:
        if c in ['a','e','i','o','u']:
            return True
    return False

def is_three_series_letter(s):
    consonants = 0
    vowels = 0
    for c in s:
        if c in ['a','e','i','o','u']:
            vowels += 1
            consonants = 0
        else:
            consonants += 1
            vowels = 0
        if vowels >= 3 or consonants >= 3:
            return True
    return False

def is_continuous_same_letter(s):
    for i in range(1, len(s)):
        if s[i] == s[i-1] and s[i] not in ['e', 'o']:
            return True
    return False


def is_acceptable(s):
    return is_in_vowel(s) and not is_three_series_letter(s) and not is_continuous_same_letter(s)

while True:
    s = input()
    if s == 'end':
        break
    if is_acceptable(s):
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
