file1 = open('input', 'r')
Lines = file1.readlines()
 
inputNums = []

def splitByInt(line, deli):
    line = line.strip()
    line = line.split(deli)
    out = []
    for i in line:
        if i != '':
            out.append(int(i))
    return out


inputNums = splitByInt(Lines[0], ',')

print(inputNums)

boards = []
idx = 0
tboard = []

for i in range(2,len(Lines)):
    if len(Lines[i]) == 1:
        boards.append(tboard)
        tboard = []
        continue

    arr = splitByInt(Lines[i], ' ')
    tboard.append(arr)
boards.append(tboard)

def checkRowOrCol(visited):
    for i in range(5):
        r = True
        c = True
        for j in range(5):
            if visited[i][j] == False:
                r = False
            if visited[j][i] == False:
                c = False
        if r or c:
            return True
    
    return False

def solveBoard(bidx):
    visited = [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]
    curBrd = boards[bidx]
    for i in range(len(inputNums)):
        for j in range(5):
            for k in range(5):
                #import pdb; pdb.set_trace()
                if curBrd[j][k] == inputNums[i]:
                    visited[j][k] = True
                    break
            else:
                continue
            break
        if i >= 5:
            if checkRowOrCol(visited):
                return i, visited

    return -1, visited

curLowestSolvedidx = 0
curVisitedBoard = []
curSolvedBoardIdx = -1
for i in range(len(boards)):
    solvedIdx, visited = solveBoard(i)
    #import pdb; pdb.set_trace()
    if solvedIdx > 0:
        if solvedIdx > curLowestSolvedidx:
            curLowestSolvedidx = solvedIdx
            curVisitedBoard = visited
            curSolvedBoardIdx = i

print(boards[curSolvedBoardIdx])
print(curLowestSolvedidx)
print(curVisitedBoard)

sumOfUnmarked = 0
for i in range(5):
    for j in range(5):
        if curVisitedBoard[i][j] == False:
            sumOfUnmarked += boards[curSolvedBoardIdx][i][j]

print(sumOfUnmarked*inputNums[curLowestSolvedidx])