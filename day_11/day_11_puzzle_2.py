import numpy as np


def read_instructions(filename):
    monkeys = {}
    monkey = None
    for line in open(filename).read().splitlines():
        splits = line.replace(',', '').split()
        if 'Monkey' in line:
            monkey = splits[-1].replace(':', '')
            monkeys[monkey] = {}
            monkeys[monkey]['count'] = 0
        elif 'Starting items' in line:
            i = splits.index('items:')
            monkeys[monkey]['items'] = np.asarray([float(split) for split in splits[i + 1:]])
        elif 'Operation' in line:
            monkeys[monkey]['operation'] = {}
            monkeys[monkey]['operation']['left'] = float(splits[-3]) if splits[-3].isnumeric() else splits[-3]
            monkeys[monkey]['operation']['symbol'] = splits[-2]
            monkeys[monkey]['operation']['right'] = float(splits[-1]) if splits[-1].isnumeric() else splits[-1]
        elif 'Test' in line:
            monkeys[monkey]['test_value'] = int(splits[-1])
        elif 'true' in line:
            monkeys[monkey]['test_true'] = splits[-1]
        elif 'false' in line:
            monkeys[monkey]['test_false'] = splits[-1]

    return monkeys


def throw_items(monkeys, n_rounds):
    n_items = sum(len(monkey['items']) for monkey in monkeys.values())
    for monkey in monkeys.values():
        zero_list = np.zeros(n_items-len(monkey['items']))
        monkey['items'] = np.append(monkey['items'], zero_list)

    denominator = np.prod([monkey['test_value'] for monkey in monkeys.values()])

    for _ in range(n_rounds):
        if _ % 10 == 0:
            print(_)
            print([monkey['count'] for monkey in monkeys.values()])
        for monkey in monkeys.keys():
            monkeys[monkey]['count'] += len(monkeys[monkey]['items'][monkeys[monkey]['items'] != 0])
            for i, item in enumerate(monkeys[monkey]['items']):
                if item == 0:
                    continue
                left = item if monkeys[monkey]['operation']['left'] == 'old' else monkeys[monkey]['operation']['left']
                right = item if monkeys[monkey]['operation']['right'] == 'old' else monkeys[monkey]['operation'][
                    'right']
                match monkeys[monkey]['operation']['symbol']:
                    case '+':
                        item = (left + right) % denominator
                    case '-':
                        item = (left - right) % denominator
                    case '*':
                        item = (left * right) % denominator
                    case '/':
                        item = (left / right) % denominator

                if item % monkeys[monkey]['test_value'] == 0:
                    index = np.where(monkeys[monkeys[monkey]['test_true']]['items'] == 0)[0][0]
                    monkeys[monkeys[monkey]['test_true']]['items'][index] = item
                else:
                    index = np.where(monkeys[monkeys[monkey]['test_false']]['items'] == 0)[0][0]
                    monkeys[monkeys[monkey]['test_false']]['items'][index] = item
            monkeys[monkey]['items'] = np.zeros(n_items)

    return monkeys


def main():
    n_rounds = 20
    monkeys = read_instructions('input.txt')
    monkeys = throw_items(monkeys, n_rounds)
    counts_sorted = sorted([monkey['count'] for monkey in monkeys.values()])
    print('')
    print(counts_sorted[-1]*counts_sorted[-2])


if __name__ == '__main__':
    main()