fName = "input"
#fName = "temp"
file1 = open(fName, 'r')
Lines = file1.readlines()

InputDig = {}
ouputDig = {}
idx = 0

def popIn(i, temp):
    InputDig[i] = []
    for x in temp:
        x = x.strip()
        if x != "":
            InputDig[i].append( x)

def popOut(i, temp):
    
    ouputDig[i] = []
    for x in temp:
        x = x.strip()
        if x != "":
            ouputDig[i].append( x)

for line in Lines:
   popIn(idx, line.split('|')[0].split(" "))
   popOut(idx, line.split('|')[1].split(" "))
   idx += 1
    
print(InputDig)
print(ouputDig)



count = 0

def findWordInWord(word, wordIn):
    for x in wordIn:
        if x not in word:
            return False
    return True

#else len(word) == 6:
#    newSubs[6] = word

def analyse(givenL):
    newSubs = {}
    for word in givenL:
        if len(word) == 2:
            newSubs[1] = word
        elif len(word) == 3:
            newSubs[7] = word        
        elif len(word) == 4:
            newSubs[4] = word   
        elif len(word) == 7:
            newSubs[8] = word
        elif findWordInWord(word, newSubs[1]) and findWordInWord(word, newSubs[7]):
            # can be 0,9,3
            if len(word) == 5:
                newSubs[3] = word
            elif len(word) == 6:
                if findWordInWord(word, newSubs[4]):
                    newSubs[9] = word
                else:
                    newSubs[0] = word
        elif len(word) == 6:
            newSubs[6] = word
    
    for word in givenL:
            if len(word) == 5 and word != newSubs[3]:
                count  = 0
                for x in newSubs[9]:
                    if x not in word:
                        count+= 1
                if count > 1:
                    newSubs[2] = word
                else:
                    newSubs[5] = word
                
    return newSubs

finalDigit = []
count = 0

for idx in InputDig:
    InputDig[idx].sort(key=len)
    a = analyse(InputDig[idx])
    print(a)
    digit = ""
    easyDigits = ouputDig[idx]
    for i in range(len(easyDigits)):   
        temp = {} 
        word = easyDigits[i]
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
                if k in [0,2,3,5,6, 9]:
                    if findWordInWord(word, v) and findWordInWord( v, word):

                        digit += str(k)
                        break

    print(digit)
    finalDigit.append(digit)
sumd= 0
for x in finalDigit:
    sumd+= int(x)

print(sumd)

