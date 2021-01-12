import math

def nCr(k,n):
    return (math    .factorial(n))/(math.factorial(k) * math.factorial(n-k))

print(nCr(20,40))