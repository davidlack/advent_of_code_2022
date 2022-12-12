import string
import numpy as np
import networkx as nx

h_map = {letter: i for i, letter in enumerate(string.ascii_lowercase)}
grid = np.array([[h_map[c] if c in h_map else c for c in line] for line in open('input.txt').read().splitlines()])
start = np.where(grid == 'S')
end = np.where(grid == 'E')
grid[start] = h_map['a']
grid[end] = h_map['z']
grid = grid.astype(int)
n_rows = grid.shape[0]
n_columns = grid.shape[1]

graph = nx.DiGraph()
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if i + 1 < n_rows and grid[i + 1][j] - grid[i][j] <= 1:
            graph.add_edge((i, j), (i + 1, j), weight=grid[i + 1][j] - grid[i][j])

        if i - 1 >= 0 and grid[i - 1][j] - grid[i][j] <= 1:
            graph.add_edge((i, j), (i - 1, j), weight=grid[i - 1][j] - grid[i][j])

        if j + 1 < n_columns and grid[i][j + 1] - grid[i][j] <= 1:
            graph.add_edge((i, j), (i, j + 1), weight=grid[i][j + 1] - grid[i][j])

        if j - 1 >= 0 and grid[i][j - 1] - grid[i][j] <= 1:
            graph.add_edge((i, j), (i, j - 1), weight=grid[i][j - 1] - grid[i][j])

shortest_path = nx.shortest_path(graph, (start[0][0], start[1][0]), (end[0][0], end[1][0]))
print('First solution: {}'.format(len(shortest_path) - 1))
start_points = np.where(grid == 0)
shortest_paths = []

for i in range(len(start_points[0])):
    try:
        shortest_paths.append(nx.shortest_path(graph, (start_points[0][i], start_points[1][i]), (end[0][0], end[1][0])))
    except:
        continue

shortest_path_length = min([len(path) for path in shortest_paths])
print('Second solution: {}'.format(shortest_path_length - 1))
print('Done')
