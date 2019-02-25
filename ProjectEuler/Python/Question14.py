def isEven(n):
    if(n % 2 == 0):
        return True
    else:
        return False

def CollatzSeq(n):
    CollatzSeq = []
    CollatzSeq.append(n)
    Flag = False
    
    while (n != 1):
        if(isEven(n)):
            n = n // 2
            CollatzSeq.append(n)
        else:
            n = (3 * n) + 1
            CollatzSeq.append(n)
    return CollatzSeq

LongestCollatz = 1
LongestCollatzList = []
number = 1

for i in range (1, 1000000):
    if(len(CollatzSeq(i)) > LongestCollatz):
        number = i
        LongestCollatz = len(CollatzSeq(i))
        LongestCollatzList = CollatzSeq(i)

print(number)



