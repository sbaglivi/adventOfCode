tot = 0
with open ("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        firstRange, secondRange = line.split(',')
        firstRangeStart, firstRangeEnd = map(int, firstRange.split('-'))
        secondRangeStart, secondRangeEnd = map(int, secondRange.split('-'))
        if ((firstRangeStart <= secondRangeStart and firstRangeEnd >= secondRangeEnd) or (secondRangeStart <= firstRangeStart and secondRangeEnd >= firstRangeEnd)):
            tot += 1

    print(tot)