def returnPicks(position, friends, picks):
    sign = 1
    friend = 1
    result = []
    for i in range(1,picks+1):
        if friend == position:
            result.append(i)
        print friend
        if i != 1:
            if friend == 1 and sign == -1:
                sign = 1
                continue
            elif friend == friends and sign == 1:
                sign = -1
                continue
        friend += sign
        if friend > friends:
            friend = friends
    return result

print returnPicks(3,6,15)
print returnPicks(1,1,10)
print returnPicks(1,2,39)
print returnPicks(5,11,100)
            
        