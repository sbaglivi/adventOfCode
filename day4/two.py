tot = 0
with open ("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        firstRange, secondRange = line.split(',')
        firstRangeStart, firstRangeEnd = map(int, firstRange.split('-'))
        secondRangeStart, secondRangeEnd = map(int, secondRange.split('-'))
        if firstRangeEnd < secondRangeEnd:
            # first range end earlier, need to check if earlier than second starts
            if firstRangeEnd < secondRangeStart:
                # no overlap
                pass
            else:
                # overlap
                tot += 1
        elif secondRangeEnd < firstRangeEnd:
            # second range ends earlier, check if earlier than first range start
            if secondRangeEnd < firstRangeStart:
                #no overlap
                pass
            else:
                # overlap
                tot += 1
        else:
            # end at same value, they overlap at least in that section
            tot += 1


        # equivalent to previous if / else block in one line
        # if (firstRangeEnd < secondRangeEnd and firstRangeEnd >= secondRangeStart) or (secondRangeEnd < firstRangeEnd and secondRangeEnd >= firstRangeStart) or (firstRangeEnd == secondRangeEnd):
        #     tot += 1
    print(tot)

    """
    
    
    pairs do not overlap if one ends before the other one begins, which means smallest endOfRange is smaller than other (and or bigger ?) startOfRange
    
    
    
    
    
    
    
    
    
    
    
    """