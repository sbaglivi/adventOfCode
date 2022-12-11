import math

"""
Object can be modeled with just a number containing their worry level I think (2 obj with same worry levels are indistinguishable from text)
each monkey instead has: - items, - conditional - throw targets based on conditionals

"""

commonDiv = 1
class Monkey:
    def __init__(self, items, expression, divisor, throwTargetIds):
        self.items = items
        self.expression = expression
        self.divisor = divisor
        self.throwTargetIds = throwTargetIds
        self.itemsInspected = 0
    
    def playTurn(self, monkeys, divisor):
        for item in self.items:
            item = self.applyExpression(item)
            # item = int(item / 3)
            # item = self.simplifyItem(item, divisors)
            self.itemsInspected += 1
            item %= divisor
            if item % self.divisor == 0:
                self.throwItemTo(item, monkeys, self.throwTargetIds[0])
            else:
                self.throwItemTo(item, monkeys, self.throwTargetIds[1])
        self.items = []

    def simplifyItem(self, item, divisors):
        # print(f"simplifying {item}")
        count = 0
        while item > 10000000:
            if count > 5:
                print(f"Could not simplyfy {item}")
                return
            count += 1
            top = math.ceil(math.sqrt(item))
            # print(f"Max divisor: {top}")
            for i in range(top, -1 ,-1):
                # if i in divisors:
                #     continue
                if item % i == 0:
                    item /= i
                    break
            # print("Coult not find divisor between top and 0")
        return item
            
    def throwItemTo(self, item, monkeys, monkeyId):
        monkeys[monkeyId].items.append(item)

    def applyExpression(self, item):
        operation = self.expression["operation"]
        operand = int(self.expression["operand"]) if self.expression["operand"] != "old" else item
        if operation == "*":
            item *= operand
        elif operation == "+":
            item += operand
        else:
            print(f"Unrecognized operation: {operation}")
        return item
        
lineCount = 0
monkeys = []
items = []
expression = {}
divisor = -1
throwTargetIds = []
allDivisors = []

with open("input.txt", "r") as f:
    for line in f:
        lineOffset = lineCount % 7
        line = line.strip()
        match lineOffset:
            case 1:
                itemsString = line.split(':')[1]
                itemsList = list(map(int, itemsString.split(',')))
                items = itemsList
                print(itemsList)

            case 2:
                words = line.split(' ')
                operation, operand = words[-2:]
                expression["operation"] = operation
                expression["operand"] = operand
                print(operation, operand)

            case 3:
                divisorStr = line.split(' ')[-1]
                divisor = int(divisorStr)
                print(divisor)
            case 4 | 5:
                monkeyId = int(line.split(' ')[-1])
                throwTargetIds.append(monkeyId)
                if lineOffset == 5:
                    monkey = Monkey(items, expression, divisor, throwTargetIds)
                    monkeys.append(monkey)
                    items = []
                    expression = {}
                    allDivisors.append(divisor)
                    commonDiv *= divisor
                    divisor = -1
                    throwTargetIds = []
            case _:
                pass
        lineCount += 1
    print(monkeys)

print(f"Divisors: {allDivisors}")
for roundCount in range(10000):
    if roundCount % 50 == 0:
        print(roundCount)
    for monkey in monkeys:
        monkey.playTurn(monkeys, commonDiv)

for monkey in monkeys:
    print(monkey.itemsInspected)

itemsInspected = list(map(lambda x: x.itemsInspected, monkeys))
itemsInspected.sort()
print(itemsInspected[-2]*itemsInspected[-1])
