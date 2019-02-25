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
num = 2000000
i = 0
while(i < num):
    if(is_prime(i) == True):
        numbers.append(i)
        i+=1
    else:
        i+=1

Psum = 0
for i in numbers:
    Psum += i

print(Psum)


