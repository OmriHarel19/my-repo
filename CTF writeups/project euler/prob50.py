
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

def consecutive_prime_sum(prime,primeList):
    for i in range(len(primeList)):

        count = 0
        for j in range(i,len(primeList)):
            if sum == prime:
                return count
            if sum > prime:
                break

            sum += primeList[j]
            count += 1

    return -1

def largest_consecutive_prime_sum(primeList):
    cur_prime = 953
    max = 21

    for i in range(60000,len(primeList)):
        prime_idx = primeList.index(primeList[i])
        count = consecutive_prime_sum(primeList[i],primeList[:prime_idx])
        if count > max:
            max = count
            cur_prime = primeList[i]
        print("i",i,"primeList[i]",primeList[i],"cur_prime",cur_prime,"max",max)
    return cur_prime


def main():
    primesList = eSieve(1000000)
    print(len(primesList))
    print(largest_consecutive_prime_sum(primesList))

if __name__ == "__main__":
    main()