
primes = [2,3,5,7,11,13,17,19]
composites = [4,6,8,9,12,14,15,16,18,20]

def evenlyDivisible(target):
    evenly = True
    for n in composites:
        if target % n > 0:
            evenly = False
            break
    return evenly


step = 1
for p in primes:
    step *= p

end = False
number = 0
while not end:
    number += step
    if evenlyDivisible(number):
        end = True
        print(number)






