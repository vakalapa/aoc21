file1 = open('input', 'r')
Lines = file1.readlines()
 
arr = []
for line in Lines:
    arr.append(line.strip())


lengthofcode = len(arr[0])
l1s = 0
l0s = 0
gray = ""
eray = ""
for i in range(lengthofcode):   
    l1s = 0
    l0s = 0
    for code in arr:
        if code[i] == '1':
            l1s += 1
        else:
            l0s += 1
    if l1s > l0s:
        gray+="1"
        eray+="0"
    else:
        gray+="0"
        eray+="1"

print(int(gray,2))
print(int(eray,2))

print("Final output:")
print(int(gray,2) * int(eray,2))