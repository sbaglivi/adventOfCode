# 1 for rock, 2 paper, 3 scissors
# adversary A rock, B paper, C scissors
# me X rock, Y paper, Z scissors
score = 0
with open("adata.txt", "r") as f:
    for line in f:
        a, b = line.strip().split(' ')
        if a == 'A':
            if b == "X":
                score += (1+3)  # 1 for rock, 3 for tie
            elif b == "Y":
                score += (2+6)  # 1 rock, 6 win
            else:
                score += (3+0)  # 1 for rock
        elif a == 'B':
            if b == "X":
                score += (1+0)  # 1 for rock, 3 for tie
            elif b == "Y":
                score += (2+3)  # 1 rock, 6 win
            else:
                score += (3+6)  # 1 for rock
        elif a == 'C':
            if b == "X":
                score += (1+6)  # 1 for rock, 3 for tie
            elif b == "Y":
                score += (2+0)  # 1 rock, 6 win
            else:
                score += (3+3)  # 1 for rock
    print(score)
