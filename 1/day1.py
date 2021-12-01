
input_file = open("./input.txt")
input = input_file.readlines()

previous = int(input[0])
count = 0
for i in input:
    if int(i) > previous:
        count += 1
    previous = int(i)

print(count)
