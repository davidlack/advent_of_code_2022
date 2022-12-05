pair_tasks = [(line.split(',')[0], line.split(',')[1]) for line in open('input.txt').readlines()]
pair_tasks = [(set(range(int(pair[0].split('-')[0]),int(pair[0].split('-')[1])+1)), set(range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1])+1))) for pair in pair_tasks]
print(sum([1 for pair in pair_tasks if len(pair[0].intersection(pair[1]))!=0]))
