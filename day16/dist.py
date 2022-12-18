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

lValves = len(valves)

dist = {}
for v1 in valves:
    dist[v1] = {}
    for v2 in valves:
        dist[v1][v2] = float('inf')

for v in valves:
    dist[v][v] = 0

for v1 in valves:
    for v2 in valves[v1]['connectedValves']:
        dist[v1][v2] = 1
        dist[v2][v1] = 1

for v1 in valves:
    for v2 in valves:
        for v3 in valves:
            if dist[v2][v3] > dist[v2][v1] + dist[v1][v3]:
                dist[v2][v3] = dist[v2][v1] + dist[v1][v3]

# valvesWF = list(filter(lambda x: x['flowRate'] > 0, valves))
valvesWF = []
for valve in valves:
    if valves[valve]['flowRate'] > 0:
        valvesWF.append(valve)
valvesToOpen = valvesWF.copy()
# vars: cv, valvesToOpen, openValvesFlow, points
def play(cv, valvesToOpen, flow, points, time, saved):
    toSerialize = {'a': cv, 'b': valvesToOpen, 'c': flow, 'd': points, 'e': time}
    serialized = json.dumps(toSerialize)
    if serialized in saved:
        return saved[serialized]
    valvesToOpenL = len(valvesToOpen)
    if time == 0:
        return points
    if valvesToOpenL == 1:
        toOpen = valvesToOpen[0]
        turnsNecessary = dist[cv][toOpen] + 1 # +1 to open
        points += turnsNecessary*flow
        time -= turnsNecessary
        flow += valves[toOpen]['flowRate']
        points += time*flow
        return points
    else:
        results = []
        for valve in valvesToOpen:
            turnsNecessary = dist[cv][valve] + 1 # +1 to open
            newLeft = valvesToOpen.copy()
            newLeft.remove(valve)
            newFlow = flow+valves[valve]['flowRate']
            newPoints = points + turnsNecessary*flow
            newTime = time - turnsNecessary
            subToSerialize = {'a': valve, 'b': newLeft, 'c': newFlow, 'd': newPoints, 'e': newTime}
            subSerialized = json.dumps(subToSerialize)
            res = None
            if subSerialized in saved:
                res = saved[subSerialized]
            else:
                res = play(valve, newLeft, newFlow, newPoints, newTime, saved)
                saved[subSerialized] = res
            results.append(res)
        results.sort(reverse=True)
        saved[serialized] = results[0]
        return results[0]
print(len(valvesToOpen))

# result = play("AA", valvesToOpen, 0, 0, 30, {})
# print(result)