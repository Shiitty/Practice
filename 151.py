import math
def approximatePi(numSides):
    return  numSides * math.sin(math.pi/numSides)

print approximatePi(17280)