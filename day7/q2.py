file1 = open('input', 'r')
Lines = file1.readlines()

crabhorpos = Lines[0].split(',')
crabhorpos = [int(x) for x in crabhorpos]
'''
test = {}
curhighcount = 0
curhighval = -1
for x in crabhorpos:
    if x not in test:
        test[x] = 1
    else:
        test[x] += 1
        #import pdb; pdb.set_trace()
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
    for val in a:
        fuel = 0
        for x in crabhorpos:
            diff = abs(x-val)
            fuel += int((diff*(diff+1))/2)
        if fuel < leastF:
            leastF = fuel
            print(fuel)
            print(val)

for i in range(470,489):
    fuel = 0
    print(i)
    for x in crabhorpos:
        diff = abs(x-i)
        fuel += int((diff*(diff+1))/2)
    print(fuel)
    if fuel < leastF:
        leastF = fuel
        print(fuel)
        print(i)
'''


leastF = 9999999999999999999999
maxVal = 0
for interval in crabhorpos:
    if interval > maxVal:
        maxVal = interval
print(maxVal)
for interval in range(maxVal):
    fuel = 0
    for x in crabhorpos:
        diff = abs(x-interval)
        fuel += int((diff*(diff+1))/2)
    if fuel < leastF:
        leastF = fuel

print(leastF)

