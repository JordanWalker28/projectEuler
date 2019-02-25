def CreateSum(n, y):
    number = n**y
    sum = 0
    NumberList = [int(i) for i in str(number)]
    for i in NumberList:
        sum += i
    return sum

print(CreateSum(2,1000))

