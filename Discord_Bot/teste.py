def check_point(f_dragon, dies):
    if dies[0] == f_dragon and dies[1] == f_dragon:
        score = 5
    elif dies[0] == f_dragon:
        score = 3
        if (dies[1] % 2 == 1) and (f_dragon % 2 == 1):
            score += 1
        elif (dies[1] % 2 == 0) and (f_dragon % 2 == 0):
            score += 1
    elif dies[1] == f_dragon:
        score = 3
        if (dies[0] % 2 == 0) and (f_dragon % 2 == 0):
            score += 1
        elif (dies[0] % 2 == 1) and (f_dragon % 2 == 1):
            score += 1
    elif (dies[0] % 2 == 0) and (f_dragon % 2 == 0):
        score = 1
        if (dies[1] % 2 == 0) and (f_dragon % 2 == 0):
            score += 1
    elif (dies[1] % 2 == 1) and (f_dragon % 2 == 1):
        score = 1
        if (dies[0] % 2 == 1) and (f_dragon % 2 == 1):
            score += 1
    else:
        score = 0
    return score


score = check_point(1, [1, 5])
print("Score 4/", score)

score = check_point(3, [2, 4])
print("Score 0/", score)

score = check_point(4, [2, 5])
print("Score 1/", score)

score = check_point(3, [2, 5])
print("Score 1/", score)

score = check_point(2, [6, 4])
print("Score 2/", score)
