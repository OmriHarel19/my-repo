import math
from itertools import chain, combinations

def SieveOfEratosthenes(n):
    primeList = []
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p] == True:
            primeList.append(p)

    return primeList

def primeFactors(n):
    lst = []
    #add number of two's that divide n
    while n % 2 == 0:
        lst.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n , print i ad divide n
        while n % i == 0:
            lst.append(i)
            n = n / i

     # Condition if n is a prime
    # number greater than 2
    if n > 2:
        lst.append(int(n))

    return lst

def sublists(list):
    # list to store all the sublists
    sublist = []
    for i in range(len(list) + 1):
        for j in range(i + 1, len(list) + 1):
            if i == 0 and j == len(list): #avoid the sublist that is similar to original list
                break
            else:
                sli = list[i:j]  # make a slice of the subarray
                sublist.append(sli)  # add it to the list of sublists
    return sublist

def powerset(iterable):
    s = iterable
    lst_tuple = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    lst = [list(i) for i in lst_tuple]
    lst.pop()
    lst.pop(0)
    return lst

def sublists_to_powers(sublists):
    sublists_powers = []
    for i in range(len(sublists)):
        if len(sublists[i]) > 1: #means that in this sublist there is more than one val
            result = 1
            for x in sublists[i]:
                result = result * x # mult the values to create the power it represents
            sublists_powers.append(result)
        else:
            sublists_powers.append(sublists[i][0]) #means thas in this sublist there is one val
    return sublists_powers

def list_noDups(lst):
    return list(dict.fromkeys(lst))

def main():
    count = 0
    n = 100
    primes = SieveOfEratosthenes(n)


    grid = []
    for i in range(n):
        grid.append([True for x in range(n)] )
    print(grid)

    for i in range(n): #run on every number from 2->n (where if i represents the number (i+2) - when i is 10 the is 12
        for j in range(n): #run on every power from 2->n (where if j represents the number (j+2) - when j is 10 the is 12
            if (j+2) not in primes:
                lst = primeFactors(j+2)
                perms = powerset(lst)
                sublists_powers = sublists_to_powers(perms)
                sublists_powers_noDups = list_noDups(sublists_powers)

                for k in sublists_powers_noDups:
                    if (k < n) and ((i+2)**k) <= n:
                        grid[(i+2)**k - 2][int((j+2)/k) - 2] = False
            if grid[i][j]:  # if this is true it means that
                count += 1

    print(count)
    print(grid)

    '''
    '''


if __name__ == "__main__":
    main()


