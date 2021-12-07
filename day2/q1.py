file1 = open('input1', 'r')
Lines = file1.readlines()
 
horPos = 0
depth = 0
for line in Lines:
    input = line.split(" ")
    instruction = input[0]
    value = int(input[1])
    if instruction == "forward":
        horPos = horPos + value
    elif instruction == "up":
        depth = depth - value
    elif instruction == "down":
        depth = depth + value

    if depth < 0:
        depth = 0

print(horPos, depth)
print(horPos*depth)