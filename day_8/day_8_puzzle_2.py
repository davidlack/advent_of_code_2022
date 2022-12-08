import numpy as np

grid = np.array([[int(char) for char in line] for line in open('input.txt').read().splitlines() if line])
n_rows = grid.shape[0]
n_columns = grid.shape[1]
scenic_scores = np.zeros(grid.shape)
scenic_scores_less_i = np.empty(grid.shape)
scenic_scores_great_i = np.empty(grid.shape)
scenic_scores_less_j = np.empty(grid.shape)
scenic_scores_great_j = np.empty(grid.shape)

for i in range(n_rows):
    for j in range(n_columns):
        lesser_i_view = 0
        greater_i_view = 0
        lesser_j_view = 0
        greater_j_view = 0

        for lesser_i in reversed(range(i)):
            lesser_i_view += 1
            if grid[lesser_i, j] >= grid[i][j]:
                break

        for greater_i in range(i+1, n_rows):
            greater_i_view += 1
            if grid[greater_i, j] >= grid[i][j]:
                break

        for lesser_j in reversed(range(j)):
            lesser_j_view += 1
            if grid[i, lesser_j] >= grid[i][j]:
                break

        for greater_j in range(j+1, n_columns):
            greater_j_view += 1
            if grid[i, greater_j] >= grid[i][j]:
                break

        if lesser_i_view == 0:
            lesser_i_view = 1

        if greater_i_view == 0:
            greater_i_view = 1

        if lesser_j_view == 0:
            lesser_j_view = 1

        if greater_j_view == 0:
            greater_j_view = 1

        scenic_scores[i][j] = lesser_i_view*greater_i_view*lesser_j_view*greater_j_view
        scenic_scores_less_i[i][j] = lesser_i_view
        scenic_scores_great_i[i][j] = greater_i_view
        scenic_scores_less_j[i][j] = lesser_j_view
        scenic_scores_great_j[i][j] = greater_j_view

print(np.max(scenic_scores))
