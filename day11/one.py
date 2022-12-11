import re
"""
Object can be modeled with just a number containing their worry level I think (2 obj with same worry levels are indistinguishable from text)
each monkey instead has: - items, - conditional - throw targets based on conditionals

"""

class Monkey:
    def __init__(self, items, expression, divisor, throwTargetIds):
        self.items = items
        self.expression = expression
        self.divisor = divisor
        self.throwTargetIds = throwTargetIds
        self.itemsInspected = 0
    
    def playTurn(self, monkeys):
        for item in self.items:
            item = self.applyExpression(item)
            item = int(item / 3)
            self.itemsInspected += 1
            if item % self.divisor == 0:
                self.throwItemTo(item, monkeys, self.throwTargetIds[0])
            else:
                self.throwItemTo(item, monkeys, self.throwTargetIds[1])
        self.items = []
            
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
                    divisor = -1
                    throwTargetIds = []
            case _:
                pass
        lineCount += 1
    print(monkeys)

for roundCount in range(20):
    for monkey in monkeys:
        monkey.playTurn(monkeys)

for monkey in monkeys:
    print(monkey.itemsInspected)

itemsInspected = list(map(lambda x: x.itemsInspected, monkeys))
itemsInspected.sort()
print(itemsInspected[-2]*itemsInspected[-1])
