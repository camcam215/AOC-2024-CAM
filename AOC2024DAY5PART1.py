from common import load_input

input = load_input()

split_input = input.split('\n\n')

rules_messy = split_input[0]

updates_messy = split_input[1]

rules_less_messy = rules_messy.split('\n')

updates_less_messy = updates_messy.split('\n')

rules = []

for pair in rules_less_messy:
    pair = pair.split('|')
    pair = list(map(int, pair))
    rules += [pair]

updates = []

for update in updates_less_messy:
    update = update.split(',')
    update = list(map(int, update))
    updates += [update]

accepted_updates = []
error_updates = []

for update in updates:
    Pass = True
    for rule in rules:
        x = rule[0]
        y = rule[1]
        if x in update and y in update:
            x_index = update.index(x)
            y_index = update.index(y)
            if x_index >= 0 and y_index >= 0:
                if x_index < y_index:
                    Pass = True
                else:
                    Pass = False
                    break
    if Pass == False:
        error_updates += [update]
    elif Pass == True:
        accepted_updates += [update]

total = 0

for update in accepted_updates:
    middle_index = round((len(update) - 1) / 2)
    total += update[middle_index]

print(total)




