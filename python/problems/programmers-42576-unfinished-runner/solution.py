def solution(participant, completion):
    answer = ''

    counts = {}
    for i in participant:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    for i in completion:
        counts[i] -= 1

    for i in counts:
        if counts[i] == 1:
            return i
