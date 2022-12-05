pair_tasks = [(line.split(',')[0], line.split(',')[1]) for line in open('input.txt').readlines()]
pair_tasks = [([int(pair[0].split('-')[0]),int(pair[0].split('-')[1])], [int(pair[1].split('-')[0]), int(pair[1].split('-')[1])]) for pair in pair_tasks]
print(sum([1 for pair in pair_tasks if (((pair[0][0] <= pair[1][0]) & (pair[1][1] <= pair[0][1])) | ((pair[1][0] <= pair[0][0]) & (pair[0][1] <= pair[1][1])))]))
