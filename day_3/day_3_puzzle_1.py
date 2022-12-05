priorities = {char: i+1 for i, char in enumerate('abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper())}
contents = [list(set(line[:len(line)//2]).intersection(line[len(line)//2:]))[0] for line in open('input.txt').readlines()]
print('Total: {}'.format(sum(priorities[item] for item in contents)))
