file1 = open('input', 'r')
Lines = file1.readlines()

initialState = Lines[0].split(',')
initialState = [int(x) for x in initialState]


for i in range(80):
    print(i)
    for idx in range(len(initialState)):
        if initialState[idx] == 0:
            initialState[idx] = 6
            initialState.append(8)
        else:
            initialState[idx] -= 1

print(len(initialState))