def enclosedVolume(Apoints, Bpoints):
    volumA = abs((Apoints[3]-Apoints[0]) * (Apoints[4]-Apoints[1]) * (Apoints[5]-Apoints[2]))
    volumB = abs((Bpoints[3]-Bpoints[0]) * (Bpoints[4]-Bpoints[1]) * (Bpoints[5]-Bpoints[2]))
    totalVolum = volumA + volumB
    c1 = max(Apoints[0],Bpoints[0])
    c2 = max(Apoints[1],Bpoints[1])
    c3 = max(Apoints[2],Bpoints[2])
    c4 = min(Apoints[3],Bpoints[3])
    c5 = min(Apoints[4],Bpoints[4])
    c6 = min(Apoints[5],Bpoints[5])
    if c1>=c4 or c2>=c5 or c3>=c6:
        return totalVolum
    interVolum = abs((c4-c1)*(c5-c2)*(c6-c3))
    return totalVolum - interVolum

print enclosedVolume([0,0,0,10,10,10],[-10,-10,-10,0,0,0])
print enclosedVolume([10,10,10,10,10,10],[-10,-10,-10,0,0,0])
print enclosedVolume([0,0,0,10,10,10],[-5,-5,-5,5,5,5])
print enclosedVolume([-10,-10,-10,10,10,10],[-5,-5,-5,5,5,5])