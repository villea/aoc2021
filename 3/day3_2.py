input_file = open("./input.txt")
input = [line.rstrip() for line in input_file]
limit = int(len(input) / 2)
row_size = len(input[0])
remaining_max = input
remaining_min = input

for column in range(row_size):
    if len(remaining_max) > 1:
        sum = 0
        for row in remaining_max:
            sum += int(row[column])
        limit = len(remaining_max) / 2
        if sum >= limit:
            remaining_max = list(
                filter(lambda r: int(r[column]) == 1, remaining_max))
        else:
            remaining_max = list(
                filter(lambda r: int(r[column]) == 0, remaining_max))
    if len(remaining_min) > 1:
        sum = 0
        for row in remaining_min:
            sum += int(row[column])
        limit = len(remaining_min) / 2
        if sum >= limit and len(remaining_min) > 1:
            remaining_min = list(
                filter(lambda r: int(r[column]) == 0, remaining_min))
        else:
            remaining_min = list(
                filter(lambda r: int(r[column]) == 1, remaining_min))

print(int(remaining_max[0], 2) * int(remaining_min[0], 2))
