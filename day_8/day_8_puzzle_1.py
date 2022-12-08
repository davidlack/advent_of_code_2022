import numpy as np

grid = np.array([[int(char) for char in line] for line in open('input.txt').read().splitlines() if line])
n_rows = grid.shape[0]-1
n_columns = grid.shape[1]-1

visible_trees = {(0, 0)}
visible_trees_list = []
for i in range(n_columns+1):
    current_height_left_to_right = -1
    current_height_right_to_left = -1
    for j in range(n_rows+1):
        print(grid[i][n_rows-j])
        if grid[i][j] > current_height_left_to_right:
            current_height_left_to_right = grid[i][j]
            visible_trees.add((i, j))

        if grid[i][n_rows-j] > current_height_right_to_left:
            current_height_right_to_left = grid[i][n_rows-j]
            visible_trees.add((i, n_rows-j))

for j in range(n_rows+1):
    current_height_top_bottom = -1
    current_height_bottom_to_top = -1
    for i in range(n_columns+1):
        if grid[i][j] > current_height_top_bottom:
            current_height_top_bottom = grid[i][j]
            visible_trees.add((i, j))
            visible_trees_list.append((i, j))

        if grid[n_columns-i][j] > current_height_bottom_to_top:
            current_height_bottom_to_top = grid[n_columns-i][j]
            visible_trees.add((n_columns-i, j))

print(len(visible_trees))
