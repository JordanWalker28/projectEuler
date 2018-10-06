def isPalindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False

i = 100
j = 100
largest = 0
while (i <= 999):
    while (j <= 999):
        sum = i * j
        if (sum > largest and isPalindrome(str(sum))):
            largest = sum
        j += 1
    j = 100
    i += 1
print (largest)





