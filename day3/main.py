# ASCII a-z = 97-122 A-Z = 65-90 
# A must = 27, a = 1    ord - 38 if uppder, ord - 96 if lower
# convert char to int: ord(c)

tot = 0
# count = 0
with open("input.txt", "r") as f:
    for line in f:
        # if count > 10:
        #     break
        # count += 1
        line = line.strip()
        half = int(len(line)/2)
        repeatingC = False
        for c in line[:half]:
            if repeatingC:
                break
            for otherC in line[half:]:
                if otherC == c:
                    repeatingC = c
                    break
        print(line)
        print(repeatingC)
        print(ord(repeatingC))
        print("==================")
        asciiVal = ord(repeatingC)
        if asciiVal >= 65 and asciiVal <= 90:
            tot += (asciiVal - 38)
        elif asciiVal >= 97 and asciiVal <= 122:
            tot += (asciiVal - 96)
        else:
            print("Character is not a letter")
            break
    print(tot)