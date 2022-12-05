priorities = {char: i+1 for i, char in enumerate('abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper())}
contents = [line.replace('\n','') for line in open('input.txt').readlines()]
badges = [list(set(contents[i]).intersection(contents[i+1]).intersection(contents[i+2]))[0] for i in range(0,len(contents),3)]
print('Total: {}'.format(sum(priorities[badge] for badge in badges)))
