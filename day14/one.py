import sys
sandExitPoint = (500,0)

# matrix = [['.' for i in range(100)] for j in range(100)]

def getPoint(x,y):
    pass
    # want it centered around 450, maybe 200 in height?
    # retun matrix[x-450, y]


def getLines():
    with open('input.txt','r') as f:
        lines = [line.strip() for line in f.readlines()]
        return lines

lines = getLines()
pointLines = []
minX = None
minY = None
maxX = None
maxY = None
for line in lines:
    linePoints = []
    pointStrings = line.split(' -> ')
    for pointString in pointStrings:
        point = tuple(map(int, pointString.split(',')))
        if minX == None or point[0] < minX:
            minX = point[0]
        if minY == None or point[1] < minY:
            minY = point[1]
        if maxX == None or point[0] > maxX:
            maxX = point[0]
        if maxY == None or point[1] > maxY:
            maxY = point[1]
        linePoints.append(point)
    pointLines.append(linePoints)
    # print(points)
print('x:',minX, maxX)
print('y:',minY, maxY)

minY = 0 # Trying to reset this otherwise some things dont work
minX -= 5
maxX += 5
oldMaxY = maxY
maxY += 5
width = maxX - minX
height = maxY - minY

matrix = [['.' for i in range(width+1)] for y in range(height+1)]
def printMatrix():
    # lines = []
    for i in range(minY, maxY+1):
        # line = []
        for y in range(minX, maxX+1):
            # line.append(y)
            print(get(y,i), end="", flush=True)
        print("", flush=True)
    #     lines.append(line)
    # print(lines)
def get(x,y):
    if (y-minY < 0) or (y-minY > len(matrix)):
        print('y out of bounds',y)
    elif (x-minX < 0) or (x-minX > len(matrix[0])):
        print('x out of bounds',x)

    # print(f'get x to "{x}" and y to "{y}"')
    # if ((y-minY) < 0) or ((x-minX) < 0) or ((y-minY) >= len(matrix)) or ((x-minX) >= len(matrix[0])):
    #     print(x,y)
    #     printMatrix()

    return matrix[y-minY][x-minX]
def set(x,y,v):
    if (y-minY < 0) or (y-minY >= len(matrix)):
        print('y out of bounds',y)
    elif (x-minX < 0) or (x-minX >= len(matrix[0])):
        print('x out of bounds',x)
    # print(f'set x to "{x}" and y to "{y}"')
    # if ((y-minY) < 0) or ((x-minX) < 0) or ((y-minY) >= len(matrix)) or ((x-minX) >= len(matrix[0])):
    #     print(x,y)
    #     printMatrix()
    matrix[y-minY][x-minX] = v

for pointLine in pointLines:
    for i in range(len(pointLine)-1):
        firstPoint = pointLine[i]
        secondPoint = pointLine[i+1]
        if firstPoint[0] == secondPoint[0]:
            if firstPoint[1] < secondPoint[1]:
                for y in range(firstPoint[1], secondPoint[1]+1):
                    set(firstPoint[0], y, '#')
            else:
                for y in range(secondPoint[1], firstPoint[1]+1):
                    set(firstPoint[0], y, '#')
        else:
            if firstPoint[0] < secondPoint[0]:
                for x in range(firstPoint[0], secondPoint[0]+1):
                    set(x, firstPoint[1], '#')
            else:
                for x in range(secondPoint[0], firstPoint[0]+1):
                    set(x, firstPoint[1], '#')

lowestSand = 0
sandCount = 0

print("Starting to pour the sand")
while lowestSand < oldMaxY:
    if sandCount % 100 == 0:
        print(sandCount, lowestSand, maxY, 'matrix now')
        printMatrix()
    if sandCount > 1000:
        break
    sandX, sandY = 500, 0
    set(sandX, sandY, '+')
    canGoDown = get(sandX, sandY+1) == '.'
    canGoDownLeft = get(sandX-1, sandY+1) == '.'
    canGoDownRight = get(sandX+1, sandY+1) == '.'
    while sandY+1 <= maxY and (canGoDown or canGoDownLeft or canGoDownRight):
        set(sandX, sandY, '.')
        if canGoDown:
            sandY += 1
        elif canGoDownLeft:
            sandX -= 1
            sandY += 1
        else:
            sandX += 1
            sandY += 1
        set(sandX, sandY, '+')
        if sandY+1 <= maxY:
            canGoDown = get(sandX, sandY+1) == '.'
            if sandX-1 >= minX:
                canGoDownLeft = get(sandX-1, sandY+1) == '.'
            if sandX+1 <= maxX:
                canGoDownRight = get(sandX+1, sandY+1) == '.'
    
    sandCount += 1
    if sandY > lowestSand:
        lowestSand = sandY
printMatrix()
print(oldMaxY)
print(minX, maxX)
print(minY, maxY)
print(sandCount-1) # kind of don't ask me why it's a -1. it just 'works' (realistically it's because it only stops when one ball too much is falling out)