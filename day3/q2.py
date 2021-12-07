file1 = open('input', 'r')
Lines = file1.readlines()
 
arr = []
for line in Lines:
    arr.append(line.strip())

def getMostOrLeastCommon(arr, mostCommon):
    l1s = 0
    l0s = 0
    val = "0"
    for code in arr:
        if code[i] == '1':
            l1s += 1
        else:
            l0s += 1
    if l1s >= l0s:
        val = "1"
    
    if mostCommon:
        return val
    else:
        if val == "1":
            return "0"
        else:
            return "1"

lengthofcode = len(arr[0])
osrr = arr 
carr = arr
for i in range(lengthofcode):
    bitToCheck = getMostOrLeastCommon(osrr, True)
    tarr = []    
    if len(osrr) > 1:        
        for code in osrr:
            if code[i] == bitToCheck:
                tarr.append(code)
        osrr = tarr
    tarr = []    
    bitToCheck = getMostOrLeastCommon(carr, False)
    if len(carr) == 1:
        continue
    for code in carr:
        if code[i] == bitToCheck:
            tarr.append(code)

    carr = tarr

print(osrr)
print(carr)

print("Final output:")
print(int(osrr[0],2) * int(carr[0],2))

