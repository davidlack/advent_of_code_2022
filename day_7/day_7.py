file_paths_and_sizes = {}
directories = []
filesystem_size = 70000000
update_size = 30000000

for line in open('input.txt').read().splitlines():
    if '$ cd ..' in line:
        directories.pop()
    elif '$ cd ' in line:
        directories.append(line[5:] + '/' if line[5:] != '/' else '/')
    elif line.split(' ')[0].isnumeric():
        file_name = line.split(' ')
        for i in range(len(directories)):
            directory = ''.join([directory for directory in directories[:len(directories) - i]])
            if directory in file_paths_and_sizes:
                file_paths_and_sizes[directory] += int(file_name[0])
            else:
                file_paths_and_sizes[directory] = int(file_name[0])

total_size = sum((value for key, value in file_paths_and_sizes.items() if value <= 100000))
print('Total size of directories <= 100000: {}'.format(total_size))

remaining = filesystem_size-file_paths_and_sizes['/']
space_needed = update_size-remaining
min_size = min([size for directory, size in file_paths_and_sizes.items() if size >= space_needed])
print('Min size of directories >= 30000000: {}'.format(min_size))
