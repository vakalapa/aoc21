file1 = open('input', 'r')
Lines = file1.readlines()

initialState = Lines[0].split(',')
initialState = [int(x) for x in initialState]

fishes = {}

for i in range(9):
    fishes[i] = 0

for i in initialState:
    fishes[i] += 1

for i in range(256):
    newFish = fishes[0]
    fishes[0] = fishes[1]
    fishes[1] = fishes[2]
    fishes[2] = fishes[3]
    fishes[3] = fishes[4]
    fishes[4] = fishes[5]
    fishes[5] = fishes[6] 
    fishes[6] = fishes[7] + newFish
    fishes[7] = fishes[8]
    fishes[8] = newFish



count  = 0
for _, v in fishes.items():
    count+=v
print(count)