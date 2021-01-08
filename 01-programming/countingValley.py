

def countingValleys(n, s):
    if n <= 0:
        return 0
    state = 0
    altitude = 0
    numValleys = 0
    for c in s:
        assert (c == 'U' or c == 'D'), "Invalid letter"
        if state == 0:
            if c == 'U':
                altitude += 1
                state = 1
            else:
                altitude -= 1
                state = 2
        elif state == 1:
            if c == 'U':
                altitude += 1
            else:
                altitude -= 1
                if altitude == 0:
                    state = 0
        else:
            if c == 'D':
                altitude -= 1
            else:
                altitude += 1
                if altitude == 0:
                    numValleys += 1
                    state = 0
    return numValleys

n = 8
s = "UDDDUDUU"
result = countingValleys(n, s)
print(f'result = {result}')
