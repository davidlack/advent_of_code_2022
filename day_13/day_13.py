from functools import cmp_to_key


def compare_items(list_1, list_2):
    if isinstance(list_1, int) and isinstance(list_2, int):
        if list_1 > list_2:
            return 1
        elif list_1 < list_2:
            return -1
        else:
            return 0
    elif isinstance(list_1, list) and isinstance(list_2, list):
        for item_1, item_2 in zip(list_1, list_2):
            comparison = compare_items(item_1, item_2)
            if comparison != 0:
                return comparison
        return compare_items(len(list_1), len(list_2))
    elif isinstance(list_1, int):
        return compare_items([list_1], list_2)
    elif isinstance(list_2, int):
        return compare_items(list_1, [list_2])


def main():
    inputs = [eval(line) for line in open('input.txt').read().splitlines() if line != '']
    dividers = [[[2]], [[6]]]
    indices = [int(i/2+1) for i in range(0, len(inputs), 2) if compare_items(inputs[i], inputs[i+1]) == -1]
    print('Part 1 = {}'.format((sum(indices))))
    inputs_with_dividers = inputs + dividers
    inputs_with_dividers.sort(key=cmp_to_key(compare_items))
    print('Part 2 = {}'.format((inputs_with_dividers.index(dividers[0])+1)*(inputs_with_dividers.index(dividers[1])+1)))
    print('Done!')


if __name__ == '__main__':
    main()
