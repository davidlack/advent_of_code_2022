import math

monkeys = {}
n_rounds = 20

monkey = None
for line in open('input.txt').read().splitlines():
    splits = line.replace(',', '').split()
    if 'Monkey' in line:
        monkey = splits[-1].replace(':', '')
        monkeys[monkey] = {}
        monkeys[monkey]['count'] = 0
    elif 'Starting items' in line:
        i = splits.index('items:')
        monkeys[monkey]['items'] = [int(split) for split in splits[i + 1:]]
    elif 'Operation' in line:
        monkeys[monkey]['operation'] = {}
        monkeys[monkey]['operation']['left'] = int(splits[-3]) if splits[-3].isnumeric() else splits[-3]
        monkeys[monkey]['operation']['symbol'] = splits[-2]
        monkeys[monkey]['operation']['right'] = int(splits[-1]) if splits[-1].isnumeric() else splits[-1]
    elif 'Test' in line:
        monkeys[monkey]['test_value'] = int(splits[-1])
    elif 'true' in line:
        monkeys[monkey]['test_true'] = splits[-1]
    elif 'false' in line:
        monkeys[monkey]['test_false'] = splits[-1]

for _ in range(n_rounds):
    for monkey in monkeys.keys():
        monkeys[monkey]['count'] += len(monkeys[monkey]['items'])
        while len(monkeys[monkey]['items']) > 0:
            item = monkeys[monkey]['items'][0]
            left = item if monkeys[monkey]['operation']['left'] == 'old' else monkeys[monkey]['operation']['left']
            right = item if monkeys[monkey]['operation']['right'] == 'old' else monkeys[monkey]['operation']['right']
            match monkeys[monkey]['operation']['symbol']:
                case '+':
                    item = math.floor((left+right) / 3.)
                case '-':
                    item = math.floor((left - right) / 3.)
                case '*':
                    item = math.floor((left * right) / 3.)
                case '/':
                    item = math.floor((left / right) / 3.)

            if item % monkeys[monkey]['test_value'] == 0:
                monkeys[monkeys[monkey]['test_true']]['items'].append(item)
                monkeys[monkey]['items'].pop(0)
            else:
                monkeys[monkeys[monkey]['test_false']]['items'].append(item)
                monkeys[monkey]['items'].pop(0)
            i += 1

counts_sorted = sorted([monkey['count'] for monkey in monkeys.values()])
print(counts_sorted[-1]*counts_sorted[-2])