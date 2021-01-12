
import math

def eSieve(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    #return a list with all prime up to n
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    primeList = []
    for i in range(len(prime)):
        if prime[i]:
            primeList.append(i)
    return primeList


def d(n):
    # returns the sum of all proper divisors of n
    sum = 1
    if n%2 != 0:
        for i in range(3,int(math.sqrt(n)),2):
            if n%i == 0:
                sum  += i + n/i
    else:
        sum += 2 + n/2
        for i in range(3, int(math.sqrt(n))):
            if n % i == 0:
                sum += i + n / i
    return sum

def sumOfAmicable(limit):
    sum = 0
    #sums all the amicable pairs under limit
    for i in range (2,limit+1):
        sum1 = d(i)
        if sum1 > i and sum1 <= limit:
            sum2 = d(sum1)
            if sum2 == i:
                sum += i + sum1
    return sum

print(sumOfAmicable(10000))