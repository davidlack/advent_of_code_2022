moves = {(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)}
lead_moves = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
n_knots = 9
current_loc = [[0, 0] for _ in range(1+n_knots)]
visited = [{(0, 0)} for _ in range(1+n_knots)]

for line in open('input.txt').read().splitlines():
    splits = line.split()
    for i in range(int(splits[1])):
        current_loc[0][0] += lead_moves[splits[0]][0]
        current_loc[0][1] += lead_moves[splits[0]][1]
        visited[0].add((current_loc[0][0], current_loc[0][1]))
        for j in range(1, n_knots+1):
            if (abs(current_loc[j-1][0]-current_loc[j][0]) <= 1 and abs(current_loc[j-1][1]-current_loc[j][1]) <= 1) \
                    or current_loc[j-1] == current_loc[j]:
                break
            best_move = None
            best_dist = 99999
            for move in moves:
                x = current_loc[j][0] + move[0]
                y = current_loc[j][1] + move[1]
                dist = abs(current_loc[j-1][0] - x) + abs(current_loc[j-1][1] - y)
                if dist < best_dist:
                    best_dist = dist
                    best_move = move

            current_loc[j][0] += best_move[0]
            current_loc[j][1] += best_move[1]
            visited[j].add((current_loc[j][0], current_loc[j][1]))

print(len(visited[-1]))


