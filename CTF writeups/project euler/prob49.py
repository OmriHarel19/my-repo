
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

def primePerms(n):
    primes = eSieve(n)
    index = 0
    for j in primes:
        if j > 1000:
            index = primes.index(j)
            break
    primes = [set(i) for i in primes[index:]]
    #for i in primes:
