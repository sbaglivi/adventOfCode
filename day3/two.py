# ASCII a-z = 97-122 A-Z = 65-90 
# A must = 27, a = 1    ord - 38 if uppder, ord - 96 if lower
# convert char to int: ord(c)

"""
se non c'e' lo inserisco e setto il valore della lettera e di count a 1
"""

tot = 0
count = 0
elfItems = {}
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        foundInLine = []
        for c in line:
            if c in elfItems:
                if c not in foundInLine:
                    elfItems[c] += 1
            else:
                elfItems[c] = 1
            foundInLine.append(c)
        count += 1 
        if (count % 3) == 0:
            commonC = ""
            for k in elfItems:
                if elfItems[k] == 3:
                    commonC = k
                    break;
            if commonC == "":
                print(count)
                print(elfItems)
                break
            
            asciiVal = ord(commonC)
            if asciiVal >= 65 and asciiVal <= 90:
                tot += (asciiVal - 38)
            elif asciiVal >= 97 and asciiVal <= 122:
                tot += (asciiVal - 96)
            else:
                print("Character is not a letter")
                break
            elfItems = {}
    print(tot)