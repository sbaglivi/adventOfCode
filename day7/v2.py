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


def findFoldersSize(fold, acc=0):
    size = 0
    for file in fold:
        if file[-1] == '/':
            dirSize, acc = findFoldersSize(fold[file], acc)
            print(f"{file}: {dirSize}")
            size += dirSize
        else:
            size += fold[file]
    if (size <= 100000):
        acc += size
    return size, acc


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
                    pathFragments = [
                        x+'/' for x in currentDir.split('/')[1:-1]]  # By doing this I'm using paths itself as the root dir ('/'), otherwise I can do [:-1] but then I end up with one more level at root of obj which is kind of redundant
                    print(
                        f"Received command `cd {argument}` so changed directory to {currentDir}")
                elif line[2:4] == "ls":
                    print("===============")
                    print(f"{currentDir} contains:")
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
    print("foldes:")
    size, acc = findFoldersSize(paths)
    print(f"/: {size}")
    print(acc)
    # print(getDirectorySizes(paths, 0))


# parseInput("test.txt")
parseInput("input.txt")
