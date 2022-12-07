file_paths_and_sizes = {}
current_directory = '/'
current_path = ''

for line in open('input.txt').readlines():
    line = line.strip()
    if '$ cd ..' in line:
        folders_in_path = list(filter(None, current_path.split('/')))
        folders_in_path.pop()
        current_path = '/' + ''.join(path + '/' for path in folders_in_path)
        if len(folders_in_path) > 0:
            current_directory = folders_in_path[-1] + '/'
        else:
            current_directory = '/'
    elif '$ cd ' in line:
        if line[5:] != '/':
            current_directory = line[5:]+'/'
        current_path += current_directory
    elif line.split(' ')[0].isnumeric():
        file_name = line.split(' ')
        if current_path in file_paths_and_sizes:
            file_paths_and_sizes[current_path] += int(file_name[0])
        else:
            file_paths_and_sizes[current_path] = int(file_name[0])

        folders_in_path = reversed(list(filter(None, current_path.split('/'))))
        previous_path = current_path
        for folder in folders_in_path:
            previous_path = previous_path[:len(previous_path)-(len(folder)+1)]
            if len(previous_path) > 0:
                if previous_path in file_paths_and_sizes:
                    file_paths_and_sizes[previous_path] += int(file_name[0])
                else:
                    file_paths_and_sizes[previous_path] = int(file_name[0])

total_size = sum((value for key, value in file_paths_and_sizes.items() if value <= 100000))
print('Total size of directories <= 100000: {}'.format(total_size))

filesystem_size = 70000000
update_size = 30000000
remaining = filesystem_size-file_paths_and_sizes['/']
space_needed = update_size-remaining
min_size = min([size for dir, size in file_paths_and_sizes.items() if size >= space_needed])
print('Min size of directories >= 30000000: {}'.format(min_size))
