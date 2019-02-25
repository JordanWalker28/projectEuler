def pythag(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False

a = [x for x in range(1, 1000)]

for num in a:
    for dig in range(num, 1000 - num):
        for i in range(dig, 1000 - dig):
            if num + dig + i == 1000:
                if pythag(num, dig, i):
                    print(format(num * dig * i))
                    exit(1)
