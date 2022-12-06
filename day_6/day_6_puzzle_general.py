length = 14
file = open('input.txt', 'r')
n_chars = [next((i+length for i in range(len(line)) if len(set(line[i:i+length]))==length)) for line in file.readlines()]
print(n_chars)