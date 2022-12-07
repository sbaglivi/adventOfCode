import re
cdRegex = re.compile(r"\$ cd (.*)$")
fileRegex = re.compile(r"(\d+) (.*)$")
prevCommand = ""
currentDir = ""

paths = {
    "contains": {},
    "size": -1
}
newpaths = {
    "/": {
        "abc/": {

        },
        "ch": 432,
    }
}
"""
should I have containsDir and containsFiles or
contains and then each child has a type?

"""


def getInnerMostObject(pathFragments):
    parentObj = paths
    for fragment in pathFragments:
        parentObj = parentObj["contains"][fragment]
    return parentObj


def getDirectorySizes(direct, acc):
    size = 0
    for subdir in direct["contains"]:
        if "contains" in direct["contains"][subdir]:
            size, acc = getDirectorySizes(direct["contains"][subdir], acc)
        else:
            size += direct["contains"][subdir]["size"]
    if size <= 100000:
        acc += size
    return size, acc


def parseInput():
    # count = 0
    with open("test.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line[0] == "$":
                # if count > 10:
                #     return
                # count += 1
                if line[2:4] == "cd":
                    result = cdRegex.search(line)
                    # same as match.group(1), [0] returns whole string matched, 1 first parenthesized group
                    argument = result[1]
                    # print("command: "+argument)
                    if argument == "/":
                        currentDir = "/"
                    elif argument == "..":
                        parentDirIndex = currentDir.rfind('/', 0, -1)
                        currentDir = currentDir[:parentDirIndex+1]
                    else:
                        currentDir += (argument + '/')

                    # pathFragments = currentDir.split('/')[:-1]
                    # pathFragments[0] = "/"
                    pathFragments = [
                        x+'/' for x in currentDir.split('/')[1:-1]]  # By doing this I'm using paths itself as the root dir ('/'), otherwise I can do [:-1] but then I end up with one more level at root of obj which is kind of redundant
                    parentObj = paths
                    for fragment in pathFragments:
                        if fragment not in parentObj["contains"]:
                            parentObj["contains"][fragment] = {
                                "contains": {}, "size": -1}
                        else:
                            parentObj = parentObj["contains"][fragment]
                    print(
                        f"Received command `cd {argument}` so changed directory to {currentDir}")
                elif line[2:4] == "ls":
                    print("===============")
                    print(f"{currentDir} contains:")
                    pass  # listing
            else:  # it's output
                pathFragments = [
                    x+'/' for x in currentDir.split('/')[1:-1]]  # By doing this I'm using paths itself as the root dir ('/'), otherwise I can do [:-1] but then I end up with one more level at root of obj which is kind of redundant
                parentObj = getInnerMostObject(pathFragments)
                # print(f"parentObject is {parentObj}")
                if line[0:3] == "dir":
                    dirName = line[4:]
                    parentObj["contains"][dirName] = {
                        "contains": {}, "size": -1}
                    # print(f"directory {dirName}")
                else:
                    result = fileRegex.search(line)
                    fileSize, fileName = result[1], result[2]
                    parentObj["contains"][fileName] = {"size": int(fileSize)}
                    # print(f"fileSize: {fileSize}, fileName: {fileName}")
    print(paths)
    print(getDirectorySizes(paths, 0))


parseInput()
