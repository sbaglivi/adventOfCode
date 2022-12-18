import re, json

pattern = re.compile(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\s\S]+)')

def getLines():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

valves = {}
lines = getLines()
currentValve = "AA"
for line in lines:
    res = pattern.search(line)
    try:
        valveName, flowRateString, connectedValvesString = res.groups()
    except:
        print("PROBLEM WHILE PARSING")
        print(line)
    flowRate = int(flowRateString)
    connectedValves = connectedValvesString.split(', ')
    valve = {'flowRate': flowRate, 'connectedValves': connectedValves}
    valves[valveName] = valve

# for valve in nonZero:
#     print(valve)
def findDistances(start, valves):
    currentValve = start
    unvisited = set()
    distances = {}
    for valve in valves.keys():
        if valve != start:
            distances[valve] = float('inf')
            unvisited.add(valve)
        else:
            distances[valve] = 0
    # print(unvisited)
    connected = valves[currentValve]['connectedValves']
    while len(unvisited) > 0:
        for valveName in connected:
            # print(currentValve)
            newDistance = distances[currentValve] + 1
            if newDistance < distances[valveName]:
                # print(f'{newDistance} < {distances[valveName]} for {valveName}')
                # print(unvisited)
                distances[valveName] = newDistance
        if currentValve in unvisited:
            unvisited.remove(currentValve)
        minDistance = None
        for valve in unvisited:
            if minDistance == None or distances[valve] < distances[minDistance]:
                minDistance = valve
        if minDistance == None:
            # print(unvisited)
            break
        currentValve = minDistance
        connected = valves[currentValve]['connectedValves']
    return distances
value = 0
timeRemaining = 30
openValves = set()
openValvesFlow = 0
# first = True
# distances = findDistances("AA", valves)


valvesToOpen = []
for valve in valves:
    if valves[valve]['flowRate'] > 0:
        valvesToOpen.append(valve)

def play(valvesToOpen, currentValve="AA", openValves=[], openValvesFlow=0, points=0, timeRemaining=30, saved={}):
    # distances = findDistances(currentValve, valves)
    serial = {'valvesToOpen': valvesToOpen, 'currentValve': currentValve, 'openValves': openValves, 'openValvesFlow': openValvesFlow, 'points': points, 'timeRemaining': timeRemaining}
    serialized = json.dumps(serial)
    if serialized in saved:
        return saved[serialized]
    cvObj= valves[currentValve]
    choices = []
    if len(valvesToOpen) == 0 or timeRemaining == 0:
        return (points + timeRemaining*openValvesFlow) # nothing to do, just add the remaining poitns to be gained and end
    for valve in cvObj['connectedValves']:
        choices.append({'type': 'move', 'to': valve})
    if currentValve not in openValves and currentValve in valvesToOpen:
        choices.append({'type': 'open', 'name': currentValve})
    results = []
    for choice in choices:
        result = None
        if choice['type'] == 'move':
            result = play(valvesToOpen, choice['to'], openValves, openValvesFlow, points+openValvesFlow, timeRemaining-1, saved=saved)
        else: # Opening
            newValvesToOpen = valvesToOpen.copy()
            newValvesToOpen.remove(currentValve)
            newOpenValves = openValves.copy()
            newOpenValves.append(currentValve)
            result = play(newValvesToOpen, currentValve, newOpenValves, openValvesFlow+cvObj['flowRate'], points+openValvesFlow, timeRemaining-1, saved=saved)
        
        results.append(result)
    results.sort(reverse=True)
    saved[serialized] = results[0]
    return results[0]

print(play(valvesToOpen))