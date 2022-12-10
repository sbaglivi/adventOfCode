count = 1
x = 1
signalStrength = 0
measureAt = [20+40*x for x in range(0, 6)]
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line == "noop":
            if count in measureAt:
                print(signalStrength, count, x)
                signalStrength += count*x
            count += 1
        else:
            toBeAdded = int(line.split(' ')[1])
            for i in range(2):
                if count in measureAt:
                    print(signalStrength, count, x)
                    signalStrength += count*x
                count += 1
            x += toBeAdded
    print(signalStrength)
