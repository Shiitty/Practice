0:3746d3Hands(numPlayers, deck):
    result = []
    for i in range(0, numPlayers):
        result.append("")
    if numPlayers > len(deck):
        return result
    for (i, card) in enumerate(deck):
        result[i%numPlayers] += card
    return result

print dealHands(6, "012345012345012345")
print dealHands(4, "111122223333")
print dealHands(1, "012345012345012345")
print dealHands(6, "01234")
print dealHands(2,"")