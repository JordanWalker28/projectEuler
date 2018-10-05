n = 4000000
sum = 0
count = 0


def fibonacci(n):
    if n <=1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

while(count <= n):
    
    if (fibonacci(count) % 2 == 0):
        sum = sum + (fibonacci(count))
    count = count + 1
    if(fibonacci(count) > n):
        print("final sum is: ", sum) 
        break
        
