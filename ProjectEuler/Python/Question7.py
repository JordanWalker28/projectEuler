def is_prime(n):
    if n < 2:
        return False;
    if n % 2 == 0:
        return n == 2  # return False
    k = 3
    while k*k <= n:
        if n % k == 0:
            return False
        k += 2
    return True

numbers = []
num = 1
while (len(numbers) < 10001):
    s = str(num)
    
    if(is_prime(num) == True):
        numbers.append(num)
        num += 1
    else:
        num +=1
    

print(numbers[-1])

