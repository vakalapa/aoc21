file1 = open('input1', 'r')
Lines = file1.readlines()
 
horPos = 0
depth = 0
aim = 0
for line in Lines:
    input = line.split(" ")
    instruction = input[0]
    value = int(input[1])
    if instruction == "forward":
        horPos = horPos + value
        if aim > 0:
            depth = aim*value + depth
    elif instruction == "up":
        aim = aim - value
    elif instruction == "down":
        aim = aim + value

print(horPos, depth)
print(horPos*depth)