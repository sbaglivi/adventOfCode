maxLine = 0
char = '9'
if int(char) > maxLine:  # it's visible
    pass


def readFirstColumn(file):
    for line in file:
        line = line.strip()
        print(line[0])


def readByColumn(file):
    lineLen = len(file[0].strip())
    print(lineLen)


def findLeftVisible(trees, grid):
    for i in range(len(trees)):
        maxRow = -1
        for y in range(len(trees[i])):
            if trees[i][y] > maxRow:
                grid[i][y] = 1
                maxRow = trees[i][y]


def findRightVisible(trees, grid):
    for i in range(len(trees)):
        maxRow = -1
        for y in range(len(trees[i])-1, -1, -1):
            if trees[i][y] > maxRow:
                grid[i][y] = 1
                maxRow = trees[i][y]


def findTopVisible(trees, grid):
    for i in range(len(trees[0])):
        maxCol = -1
        for y in range(len(trees)):
            if trees[y][i] > maxCol:
                grid[y][i] = 1
                maxCol = trees[y][i]


def findBottomVisible(trees, grid):
    for i in range(len(trees[0])):
        maxCol = -1
        for y in range(len(trees)-1, -1, -1):
            if trees[y][i] > maxCol:
                grid[y][i] = 1
                maxCol = trees[y][i]


with open('input.txt', 'r') as f:
    trees = [list(map(int, list(line.strip()))) for line in f]
    rowLen = len(trees[0])
    rowNum = len(trees)
    visibleGrid = [[0 for col in range(rowLen)] for row in range(rowNum)]
    # for row in trees:
    #     print(row[rowLen-1])
    findRightVisible(trees, visibleGrid)
    findLeftVisible(trees, visibleGrid)
    findTopVisible(trees, visibleGrid)
    findBottomVisible(trees, visibleGrid)
    # for row in trees:
    #     print(row)
    # print("=============")
    totalVisible = 0
    for row in visibleGrid:
        # print(row)
        for col in row:
            totalVisible += col
    print(totalVisible)


"""
I think I need to construct a grid of 0s and 1s where 1 means visible and 0 means not visible.
Because I'm going to be checking from multiple directions and I don't want to count trees twice

Not sure if there is an alternative method that skips over looping from all directions
"""
