import re

pattern = re.compile(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\s\S]+)')

def getLines():
    with open("test.txt", "r") as f:
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
first = True
distances = findDistances("AA", valves)
while timeRemaining > 0:
    rewards = []
    for k,v in distances.items():
        reward = (timeRemaining-v-1)*valves[k]['flowRate']
        rewards.append({'name': k, 'reward': reward})
        # print(f'{k}: {v}, reward {reward}, ')
    rewards = list(filter(lambda x: x['name'] not in openValves, rewards))
    rewards.sort(key=lambda x: x['reward'], reverse=True)
    if first:
        print(rewards)
        first = False
    if len(rewards) == 0 or rewards[0]['reward'] == 0:
        print(f'no more rewards or first of rewards has flow rate = 0, {rewards}')
        value =+ timeRemaining*openValvesFlow
        break
    bestReward = rewards[0]
    rName = bestReward['name']
    openValves.add(rName)
    print(f"Opened valve {rName} with flow {valves[rName]['flowRate']}")
    value += openValvesFlow*min(distances[rName]+1, timeRemaining)
    openValvesFlow += valves[rName]['flowRate']
    timeRemaining -= (distances[rName] + 1) # time to open the valve
    distances = findDistances(rName, valves)
    print(timeRemaining)
print(value)
