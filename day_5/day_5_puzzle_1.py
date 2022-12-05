lines = [line.replace('\n', '') for line in open('input.txt').readlines()]
index = [i for line in lines if line.replace(' ', '').isnumeric() for i, char in enumerate(line) if char.isnumeric()]
boxes = [list(reversed([line[i] for line in lines if '[' in line])) for i in index]
boxes = [[box for box in column if box != ' '] for column in boxes]
instructions = [[int(number) for number in line.split(' ') if number.isnumeric()] for line in lines if 'move' in line]

for instruction in instructions:
    if len(instruction) == 3:
        boxes[instruction[2]-1] += reversed(boxes[instruction[1]-1][-instruction[0]:])
        boxes[instruction[1]-1] = boxes[instruction[1]-1][:-instruction[0]]

top = ''.join(column[-1] if len(column) > 0 else ' ' for column in boxes)
