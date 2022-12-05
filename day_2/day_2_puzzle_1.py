file = open('input.txt', 'r')
move_scores = {'X': 1, 'Y': 2, 'Z': 3}
results_map = {'AX': 3, 'BY': 3, 'CZ': 3, 'AY': 6, 'BZ': 6, 'CX': 6, 'BX': 0, 'CY': 0, 'AZ': 0}
print('Final Score: {}'.format(sum([results_map[line[0]+line[2]]+move_scores[line[2]] for line in file.readlines()])))
