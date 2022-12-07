import re
paths = {}
cdRegex = re.compile(r"\$ cd (.*)$")
fileRegex = re.compile(r"(\d+) (.*)$")
currentDir = ""


def getInnerMostObject(currentDir):
    pathFragments = [
        x+'/' for x in currentDir.split('/')[1:-1]]  # By doing this I'm using paths itself as the root dir ('/'), otherwise I can do [:-1] but then I end up with one more level at root of obj which is kind of redundant
    parentObject = paths
    for fragment in pathFragments:
        parentObject = parentObject[fragment]
    return parentObject


DIR_MIN_SIZE = 4795677

current_min = 9999999999


def findFoldersSize(fold):
    # necessary otherwise when I assign a value to it, it becomes treated as a local variable
    global current_min
    size = 0
    for file in fold:
        if file[-1] == '/':
            dirSize = findFoldersSize(fold[file])
            print(f"{file}: {dirSize}")
            size += dirSize
        else:
            size += fold[file]
    if size >= DIR_MIN_SIZE and size <= current_min:
        current_min = size
    return size


def parseInput(fileName):
    with open(fileName, "r") as f:
        for line in f:
            line = line.strip()
            if line[0] == "$":
                if line[2:4] == "cd":
                    result = cdRegex.search(line)
                    argument = result[1]
                    if argument == "/":
                        currentDir = "/"
                    elif argument == "..":
                        parentDirIndex = currentDir.rfind('/', 0, -1)
                        currentDir = currentDir[:parentDirIndex+1]
                    else:
                        currentDir += (argument + '/')
                elif line[2:4] == "ls":
                    pass  # listing
            else:  # it's output
                parentObj = getInnerMostObject(currentDir)
                # print(f"parentObject is {parentObj}")
                if line[0:3] == "dir":
                    dirName = line[4:]
                    parentObj[dirName+'/'] = {}
                else:
                    result = fileRegex.search(line)
                    fileSize, fileName = result[1], result[2]
                    parentObj[fileName] = int(fileSize)
    print("folders:")
    size = findFoldersSize(paths)
    totSize = 70000000
    spaceNeeded = 30000000
    print(f"/: {size}")
    print(f"Need to free: {spaceNeeded - (totSize - size)}")
    print(f"Size of smallest folder to delete: {current_min}")


# parseInput("test.txt")
parseInput("input.txt")
