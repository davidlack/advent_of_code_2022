file = open('input.txt', 'r')
calories = 0
calories_list = []
for line in file.readlines():
    if line != '\n':
        calories += int(line)
    else:
        calories_list.append(calories)
        calories = 0
top_3 = sorted(calories_list, reverse=True)[:3]
print(top_3[0])
print(sum(top_3))
