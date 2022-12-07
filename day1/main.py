max = 0
topThree = [0,0,0]
currentCount = 0
with open('input.txt', 'r') as f:
    for line in f:
        if line == "\n":
            if currentCount > topThree[0]:
                topThree[2] = topThree[1]
                topThree[1] = topThree[0]
                topThree[0] = currentCount
            elif currentCount > topThree[1]:
                topThree[2] = topThree[1]
                topThree[1] = currentCount
            elif currentCount > topThree[2]:
                topThree[2] = currentCount
            currentCount = 0
        else:
            currentCount += int(line)

    print(topThree[0]+topThree[1]+topThree[2])