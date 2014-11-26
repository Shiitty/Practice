def cardsLeft(deck):
    count = 0
    ind = 0
    deckNum = []
    for char in deck:
        if char == 'A':
            deckNum.append(1)
        elif  char == '2':
            deckNum.append(2)
        elif char == '3':
            deckNum.append(3)
        elif char == '4':
            deckNum.append(4)
        elif char == '5':
            deckNum.append(5)
        elif char == '6':
            deckNum.append(6)
        elif char == '7':
            deckNum.append(7)
        elif char == '8':
            deckNum.append(8)
        elif char == '9':
            deckNum.append(9)
        elif char == 'T':
            deckNum.append(10)
        elif char == 'J':
            deckNum.append(11)
        elif char == 'Q':
            deckNum.append(12)
        elif char == 'K':
            deckNum.append(13)
    while count <= len(deckNum):
        if deckNum[ind%len(deckNum)]!= 13 and deckNum[ind%len(deckNum)]+deckNum[(ind+1)%len(deckNum)]!= 13:
            count += 1
            ind += 1
            continue
        if deckNum[ind%len(deckNum)] == 13:
            deckNum.pop(ind%len(deckNum))
            count = 0
            if len(deckNum)==0:
                break
        if len(deckNum)>1:
            if deckNum[(ind+1)%len(deckNum)] + deckNum[ind%len(deckNum)] == 13:
                count = 0
                x = ind%len(deckNum)
                y = (ind+1)%len(deckNum)
                if x<y:
                    deckNum.pop(y)
                    deckNum.pop(x)
                else:
                    deckNum.pop(x)
                    deckNum.pop(y)
                if len(deckNum)==0:
                    break
    return len(deckNum)

print "result:"
print cardsLeft("KKKKKKKKKK") 
print "result:"
print cardsLeft("KKKKKAQ3")
print "result:"
print cardsLeft("KKKKATQ23J")
print "result:"
print cardsLeft("AT68482AK6875QJ5K9573Q")
print "result:"
print cardsLeft("AQK262362TKKAQ6262437892KTTJA332")
        