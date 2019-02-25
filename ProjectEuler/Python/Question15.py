import math

def LatticePath_v2(down, right):
    numPaths = 0
    return math.factorial(down + right) // (math.factorial(down)**2)

print(LatticePath_v2(20,20))
