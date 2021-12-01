
input_file = open("./input.txt")
input = input_file.readlines()

last_index = len(input) - 3

previous = 0
count = 0

for i in range(0, last_index):
    sum = 0
    for a in range(i, i+3):
        sum += int(input[a])
    if sum > previous:
        count += 1
    previous = sum

print(count)
