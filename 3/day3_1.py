input_file = open("./input.txt")
input = input_file.readlines()

limit = int(len(input) / 2)
row_size = len(input[0]) - 1

counters = [0 for i in range(row_size)]

for row in input:
    for a, b in zip(range(row_size), row):
        counters[a] += int(b)
val1 = int("".join(["1" if x > limit else "0" for x in counters]), 2)
val2 = int("".join(["0" if x > limit else "1" for x in counters]), 2)

print(val1 * val2)
