def calcScenicScore(startRow, startCol, trees):
    treeHeight = trees[startRow][startCol]
    # score right
    rightScore = 0
    for col in range(startCol+1, len(trees[startRow])):
        rightScore += 1
        if trees[startRow][col] >= treeHeight:
            break
    # score left
    leftScore = 0
    for col in range(startCol-1, -1, -1):
        leftScore += 1
        if trees[startRow][col] >= treeHeight:
            break
    # score top
    topScore = 0
    for row in range(startRow-1, -1, -1):
        topScore += 1
        if trees[row][startCol] >= treeHeight:
            break
    # score bottom
    bottomScore = 0
    for row in range(startRow+1, len(trees)):
        bottomScore += 1
        if trees[row][startCol] >= treeHeight:
            break
    totalScore = rightScore * leftScore * topScore * bottomScore
    return totalScore


def calcAllScenicScores(trees):
    max = -1
    for i in range(len(trees)):
        for y in range(len(trees[i])):
            score = calcScenicScore(i, y, trees)
            if score > max:
                max = score
    return max


with open('input.txt', 'r') as f:
    trees = [list(map(int, list(line.strip()))) for line in f]
    rowLen = len(trees[0])
    rowNum = len(trees)
    visibleGrid = [[0 for col in range(rowLen)] for row in range(rowNum)]
    maxScore = calcAllScenicScores(trees)
    print(maxScore)


"""
I think I need to construct a grid of 0s and 1s where 1 means visible and 0 means not visible.
Because I'm going to be checking from multiple directions and I don't want to count trees twice

Not sure if there is an alternative method that skips over looping from all directions
"""
