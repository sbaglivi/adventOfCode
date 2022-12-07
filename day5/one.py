import re
"""

    [C]             [L]         [T]
    [V] [R] [M]     [T]         [B]
    [F] [G] [H] [Q] [Q]         [H]
    [W] [L] [P] [V] [M] [V]     [F]
    [P] [C] [W] [S] [Z] [B] [S] [P]
[G] [R] [M] [B] [F] [J] [S] [Z] [D]
[J] [L] [P] [F] [C] [H] [F] [J] [C]
[Z] [Q] [F] [L] [G] [W] [H] [F] [M]
 1   2   3   4   5   6   7   8   9 
"""

startPosition = [
    [],  # just to keep the convention of ordinals that start at 1
    ['Z', 'J', 'G'],
    ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],
    ['F', 'P', 'M', 'C', 'L', 'G', 'R'],
    ['L', 'F', 'B', 'W', 'P', 'H', 'M'],
    ['G', 'C', 'F', 'S', 'V', 'Q'],
    ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],
    ['H', 'F', 'S', 'B', 'V'],
    ['F', 'J', 'Z', 'S'],
    ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']
]

testCase = [
    [],
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]

testInstructions = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")


def parseLine(line):
    line = line.strip()
    match = pattern.search(line)
    results = match.groups()
    if len(results) != 3:
        print(line)
        print("does not match regex")
    return map(int, results)
    nToMove, whereFrom, whereTo = map(int, results)


def runTest():
    lines = testInstructions.split('\n')
    for line in lines:
        nToMove, whereFrom, whereTo = parseLine(line)
        for i in range(nToMove):
            beingMoved = testCase[whereFrom].pop()
            testCase[whereTo].append(beingMoved)
    print(testCase)
    lastElements = [l.pop() for l in testCase if len(l) > 0]
    print(lastElements)


with open("input.txt", "r") as f:
    for line in f:
        nToMove, whereFrom, whereTo = parseLine(line)
        for i in range(nToMove):
            beingMoved = startPosition[whereFrom].pop()
            startPosition[whereTo].append(beingMoved)
    lastElements = [l.pop() for l in startPosition if len(l) > 0]
    print(lastElements)
