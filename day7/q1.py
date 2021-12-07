file1 = open('input', 'r')
Lines = file1.readlines()

crabhorpos = Lines[0].split(',')
crabhorpos = [int(x) for x in crabhorpos]

test = {}
curhighcount = 0
curhighval = -1
for x in crabhorpos:
    if x not in test:
        test[x] = 1
    else:
        test[x] += 1
        if test[x] > curhighcount:
            curhighcount = test[x]
            curhighval = x

newVals = {}

for k,v in test.items():
    if v in newVals:
        newVals[v].append(k)
    else:
        newVals[v] = [k]

leastF = 9999999999999999999999

for i in range(curhighcount, 0, -1):
    a = []
    for  v in newVals[i]:
        a.append(v)
        print(v)

    for val in a:
        fuel = 0
        for x in crabhorpos:
            fuel += abs(x-val)
        if fuel < leastF:
            leastF = fuel

print(leastF)

