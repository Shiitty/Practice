def getPrime(param):
    notyet = True
    attmpt = 0
    if param%2 == 0:
        attmpt = param + 1
    else:
        attmpt = param + 2
    if attmpt == 2 or attmpt == 3 or attmpt ==5:
        return attmpt
    attmpt - 2
    while notyet:
        attmpt += 2
        notyet = False
        for mod in range(2,attmpt/2):
            if attmpt%mod==0:
                notyet = True
                break
    return attmpt

print getPrime(13)
print getPrime(256)