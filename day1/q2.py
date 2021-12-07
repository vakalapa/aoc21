file1 = open('input2', 'r')
Lines = file1.readlines()
 
count = -1
values = []
i = 0
for line in Lines:
    values.append(int(line.strip()))

prev = 0
for i in range(1,len(values)):
    if i+1 >= len(values):
        break
    cur = values[i] + values[i-1] + values[i+1]
    print("Prev: "+str(prev)+" Cur: "+str(cur))
    if cur > prev:
        count += 1
    prev = cur
print(count)