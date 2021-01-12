
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

def isPandigital(n,dig):
    n = str(n)
    for i in range(1,dig+1):
        if n.count(str(i)) != 1:
            return False
    return True

def largest_pandig_prime(lastDig,lim):
    primes = eSieve(lim)
    for i in primes[::-1]:
        if isPandigital(i, lastDig):
            return i

#create all possible permutations for "7654321" and check for the biggest prime

def main():
    print(largest_pandig_prime(7,7654321))


if __name__ == "__main__":
    main()