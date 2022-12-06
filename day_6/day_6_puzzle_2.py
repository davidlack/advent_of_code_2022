lines = [i+14 for line in open('input.txt').readlines() for i in range(len(line)) if len(set(line[i:i+14])) == 14]
print(lines)