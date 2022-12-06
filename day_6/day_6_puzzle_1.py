print(next((i+4 for line in open('input.txt').readlines() for i in range(len(line)) if len(set(line[i:i+4])) == 4)))
