"""
Head and tail start in the same position. In the example they're showing to start in the bottom left corner although I don't think that's important
The problem asks us to count how many different positions the tail visits while following the head in its movements.
The tail must always be within 1 square of the head, vertically / hor or diagonally. They can also overlap.

If you are diagonally adjacent and head moves away the tail takes one diagonal step toward head. Example:
..      .H    .H
.H  =>  .. => .T 
T.      T.    .. 

The steps are not taken all at once (head moves by 4 to right) but instead one square at a time (head moves by 1 square to right 4 times in a row and tail follows each movement if necessary)


"""

# horizontal, vertical offset from starting position
positionsOccupied = ["0,0"]
headPos = [0,0]
tailPos = [0,0]

def serializePosition(position):
    return f"{position[0]},{position[1]}"

def calculateTailPos(tailPos, headPos):
    # NEEDS TO BE DONE
    tailOffset = [headPos[0]-tailPos[0], headPos[1]-tailPos[1]]
    if tailOffset[0] == 0: # horizontally they're on the same level
        if abs(tailOffset[1]) <= 1: # at most they're one step away: tail is fine where it is
            pass
        elif tailOffset[1] > 1: # head is above tail by more than 1 row
            tailPos[1] = headPos[1]-1 # put tail 1 row below head
        elif tailOffset[1] < -1: # head is below tail by more than 1 row
            tailPos[1] = headPos[1]+1 # put tail 1 row above head
    elif tailOffset[1] == 0: # vertical same level
        if abs(tailOffset[0]) <= 1: # at most they're one step away: tail is fine where it is
            pass
        elif tailOffset[0] > 1: # head is to the right of tail by more than 1 row
            tailPos[0] = headPos[0]-1 # put tail 1 row below head
        elif tailOffset[0] < -1: # head is to the left of tail by more than 1 row
            tailPos[0] = headPos[0]+1 # put tail 1 row above head
    else: # they're not on the same row and they're not on the same column
        if abs(tailOffset[0]) == 1 and abs(tailOffset[1]) == 1: # diagonally adjacent
            pass # this is an accepted position
        elif abs(tailOffset[0]) > 1: # they're horizontally apart by more than 1
            # diagonal move to be made here
            if tailOffset[0] > 1: # head to the right of tail by more than 1, put tail 1 to left of head
                tailPos[0] = headPos[0] - 1
            elif tailOffset[0] < -1:
                tailPos[0] = headPos[0] + 1
            tailPos[1] = headPos[1] # not 100% sure, but on the dimension where they're only 1 unit afar they should get on the same row/col
        elif abs(tailOffset[1]) > 1: # they're vertically apart by more than 1
            # diagonal move to be made here
            if tailOffset[1] > 1: # head to above tail by more than 1, put tail 1 below head
                tailPos[1] = headPos[1] - 1
            elif tailOffset[1] < -1: # head below tail by more than 1
                tailPos[1] = headPos[1] + 1
            tailPos[0] = headPos[0] # not 100% sure, but on the dimension where they're only 1 unit afar they should get on the same row/col
        else: # they should be apart by more than 1 row and more than 1 column, with only 1 move of the head this should never be possible
            print("Something went wrong, tail is more than 1 row and 1 col away from head")
        

    return tailPos

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        direction, steps = line.split(" ")
        steps = int(steps)
        for i in range(steps):
            if direction == "R":
                headPos = [headPos[0]+1, headPos[1]]
            elif direction == "L":
                headPos = [headPos[0]-1, headPos[1]]
            elif direction == "D":
                headPos = [headPos[0], headPos[1]-1]
            else:
                headPos = [headPos[0], headPos[1]+1]
            tailPos = calculateTailPos(tailPos, headPos)
            serializedTailPos = serializePosition(tailPos)
            if serializedTailPos not in positionsOccupied:
                positionsOccupied.append(serializedTailPos)
    print(len(positionsOccupied))