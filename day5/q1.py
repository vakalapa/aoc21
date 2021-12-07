file1 = open('input', 'r')
Lines = file1.readlines()
 
inputNums = []
noOfLines = 990

def splitByInt(deli=" -> "):
    inputNums = []
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
            temp["type"] = "ver"
        elif left[1] == right[1]:
            temp["type"] = "hor"
        else:            
            temp["type"] = "diag"
        inputNums.append(temp)
    return inputNums


inputNums = splitByInt()
finalVisited = []



def drawLine():
    finalVisited = []
    for i in range(noOfLines):
        temp = []
        for j in range(noOfLines):
            temp.append(0)
        finalVisited.append(temp)
    
    #import pdb;pdb.set_trace()
    for input in inputNums:
        if input["type"] == "ver":
            l = input["y1"]
            r = input["y2"]
            if input["y1"] > input["y2"]:
                l = input["y2"]
                r = input["y1"]
            for j in range(l, r+1):
                finalVisited[j][input["x1"]] += 1
        elif input["type"] == "hor":
            l = input["x1"]
            r = input["x2"]
            if input["x1"] > input["x2"]:
                l = input["x2"]
                r = input["x1"]
            for i in range(l, r+1):
                finalVisited[input["y1"]][i] += 1
        else:
            diff = input["x1"]- input["x2"]
            diff = abs(diff)
            ldiff =  input["x1"] > input["x2"]
            rdiff =  input["y1"] > input["y2"]
            for i in range(diff+1):
                l = i
                r = i
                if ldiff:
                    l = -i
                if rdiff:
                    r = -i
                finalVisited[input["y1"]+r][input["x1"]+l] += 1
    return finalVisited


finalVisited = drawLine()


count = 0 
for i in range(noOfLines):
    for j in range(noOfLines):
        if finalVisited[i][j] > 1:
            count += 1


print(count)
#print(finalVisited)