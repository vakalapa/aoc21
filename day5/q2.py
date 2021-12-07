file1 = open('input', 'r')
Lines = file1.readlines()
 
inputNums = []

def splitByInt(deli=" -> "):
    for line in Lines:
        temp = {}
        line = line.strip()
        line = line.split(deli)        
        left = line[0].split(",")
        right = line[1].split(",")
        temp["x1"] = int(left[0])
        temp["y1"] = int(left[1])
        temp["x2"] = int(right[0])
        temp["y2"] = int(right[1])
        if left[0] == right[0]:
            temp["type"] = "hor"
            inputNums.append(temp)
        elif left[1] == right[1]:
            temp["type"] = "ver"
            inputNums.append(temp)
        else:
            continue
    


splitByInt()

print(inputNums)