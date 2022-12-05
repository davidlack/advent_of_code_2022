file = open('input.txt', 'r')
move_scores = {'A': 1, 'B': 2, 'C': 3}
result_scores = {'X': 0, 'Y': 3, 'Z': 6}
strategy_map = {'X': {'A': 'C', 'B': 'A', 'C': 'B'}, 'Y': {'A': 'A', 'B': 'B', 'C': 'C'}, 'Z': {'A': 'B', 'B': 'C', 'C': 'A'}}
scores = sum([move_scores[strategy_map[line[2]][line[0]]]+result_scores[line[2]] for line in file.readlines()])
print('Final score: {}'.format(scores))
