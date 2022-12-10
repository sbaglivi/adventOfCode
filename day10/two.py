"""
map count to position on screen (+- 1 since 3 pixels at a time?)
if value of x is similar draw?

cycles (count for me) = position that's being drawn
x = position of center of sprite, that extends to -1 and +1 of x
if x-1 < count < x+1 then we draw # else .


"""
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6
screen = [['' for i in range(SCREEN_WIDTH)] for y in range(SCREEN_HEIGHT)]


def countToPixel(count):
    adjustedCount = count - 1
    row = int(adjustedCount / SCREEN_WIDTH)
    col = adjustedCount % SCREEN_WIDTH
    return row, col


def setPixel(count, value):
    row = int(count / SCREEN_WIDTH)
    col = count % SCREEN_WIDTH
    screen[row][col] = value


def main():
    count = 1
    x = 1
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            # if 15 <= count <= 17:
            #     print(x)
            #     print(line)
            if line == "noop":
                adjustedCount = count - 1
                if x - 1 <= (adjustedCount % SCREEN_WIDTH) <= x + 1:
                    setPixel(adjustedCount, '#')
                else:
                    setPixel(adjustedCount, ".")

                count += 1
            else:
                toBeAdded = int(line.split(' ')[1])
                # since array are 0 indexed but count starts at 1 and the drawing shows the first cycle draws cell #0
                for i in range(2):
                    adjustedCount = count - 1
                    if (x - 1) <= (adjustedCount % SCREEN_WIDTH) <= (x + 1):
                        setPixel(adjustedCount, '#')
                    else:
                        setPixel(adjustedCount, ".")
                    count += 1
                x += toBeAdded
        for line in screen:
            toBePrinted = ''.join(line)
            print(toBePrinted)


main()
