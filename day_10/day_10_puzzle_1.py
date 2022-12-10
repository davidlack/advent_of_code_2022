values = [1]
for line in open('input.txt').read().splitlines():
    splits = line.split()
    if splits[0] == 'noop':
        values.append(values[-1])
    elif splits[0] == 'addx':
        values.append(values[-1])
        values.append(values[-1]+int(splits[-1]))

interesting = [20, 60, 100, 140, 180, 220]
print(sum((values[i-1]*i for i in interesting)))
