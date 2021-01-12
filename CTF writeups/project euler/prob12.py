
import math

"""

my solution:

def numOfDivisors(n):
    count = 2
    if n%2 != 0:
        for i in range(3,int(math.sqrt(n))+1,2):
            if n%i == 0:
                count += 2
    else:
        count += 2
        for i in range(3,int(math.sqrt(n))+1):
            if n%i == 0:
                count += 2
    return count

def triNum(n):
    return (1+n)*(n/2)

print(eSieve(100))


bool = True
i = 10**4
while bool:
    if i > 10**5:
        bool = False
    if numOfDivisors(triNum(i)) > 500:
        print(triNum(i))
        bool = False
    i += 1

print("done")
"""

def eSieve(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
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
"""

 #using prime factorization to return the numbers of divisors of int n
def primeFactorizationNoD(n, primeList):
    numOfDiv = 1
    remain = n

    for i in primeList:


"""