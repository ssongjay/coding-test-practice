def solution(s):
    max = -1
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 1]:
            if s[i] == s[i + 2]:
                if max < int(s[i:i + 3]):
                    max = int(s[i:i + 3])

    return max
