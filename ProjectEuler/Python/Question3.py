import math
n = 600851475143

def primeFactors(n):
    largest = 0
    
    primeList = []
    while n % 2 == 0:
        primeList.insert(0, 2)
        n = n / 2
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            primeList.insert(0, i)
            n = n / i

    for x in primeList:
        if (x > largest):
            largest = x

    if largest == 0:
        largest = n

    return print(largest)

primeFactors(n)


