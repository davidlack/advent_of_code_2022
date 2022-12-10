import numpy as np
import pandas as pd

screen = np.empty((6,40), 'str')
screen[:, :] = '.'

sprite_loc = [1]

for line in open('input.txt').read().splitlines():
    splits = line.split()
    if splits[0] == 'noop':
        sprite_loc.append(sprite_loc[-1])
    elif splits[0] == 'addx':
        sprite_loc.append(sprite_loc[-1])
        sprite_loc.append(sprite_loc[-1]+int(splits[-1]))

screen_output = ['' for i in range(screen.shape[0])]
for i in range(1, screen.shape[0]+1):
    for j in range(1, screen.shape[1]+1):
        if sprite_loc[j-1] <= j <= sprite_loc[j-1]+2:
            screen[i-1, j-1] = '#'
        screen_output[i-1] += screen[i-1, j-1]
    del sprite_loc[0:40]

print(pd.DataFrame(screen_output))

