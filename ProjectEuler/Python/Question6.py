sumSquares = 0
sumFirstN = 0

for x in range(1, 101):
    sumSquares = sumSquares + (x * x)
    sumFirstN = sumFirstN + x

sumFirstN = sumFirstN * sumFirstN
print(sumFirstN - sumSquares)





