def sqrSum(n):
    return (n/6)*(n+1)*(2*n+1)

def sumSqr(n):
    return ((1+n)*(n/2))**2


print(sumSqr(100)-sqrSum(100))