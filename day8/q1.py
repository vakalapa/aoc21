fName = "input"
fName = "temp"
file1 = open(fName, 'r')
Lines = file1.readlines()

easyDigits = []
for line in Lines:
    temp = line.split('|')[1].split(" ")
    for x in temp:
        x = x.strip()
        if x != "":
            easyDigits.append(x)
print(easyDigits)





a = {
    0 : "cagedb",
    2:  "gcdfa",
    3: "fbcad",
    5:"cdfbe",
    6:"cdfgeb",
    9: "cefabd",
}

count = 0

def findWordInWord(word, wordIn):
    for x in wordIn:
        if x not in word:
            return False
    return True

finalDigit = []
count = 0
digit = ""
for i in range(len(easyDigits)):   
    temp = {} 
    word = easyDigits[i]
    if i %4 ==0:        
        if digit != "":
            finalDigit.append(digit)
        digit = ""
    for x in word:
        temp[x] = True
    
    if len(temp) == 2:
        digit+= "1"
    elif len(temp) == 3 :        
        digit+= "7"
    elif  len(temp) == 4:
        digit+= "4"    
    elif len(temp) == 7:        
        digit+= "8"    
    else:
        for k,v in a.items():
            if findWordInWord(word, v):
                digit += str(k)
                break

            print(word)

sumd= 0
for x in finalDigit:
    sumd+= int(x)

print(sumd)