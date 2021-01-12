
import math

def shrinkFact(n):
    num = 1
    for i in range(2,n+1):
        if i%10 == 0:
            num = num * (i/10)
        else:
            num = num * i
        if num%10 == 0:
            num = num/10
    return num

def amountOf2and5toDivide(n):
    multsOf2 = 2
    multsOf5 = 5
    count = 0
    while (multsOf2 < n) and (multsOf5 < n):
        count+=1
        multsOf5 = multsOf5 + 10
        multsOf2 = multsOf2 + 2
    return count

def sum_digits(n):
    n = int(n)
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print(sum_digits(math.factorial(100)))