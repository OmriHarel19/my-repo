
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

def isDivin2or5(num):
    #returns F if every possible perm of num would not divide in 2,3,5
    digs = [2,4,6,8,5,0]
    while num > 0:
        if num%10 in digs:
            return True
        num = int(num/10)
    return False

def main():
    primeList = eSieve(1000000)
    primeList = primeList[4:] #remove 2,3,5,7
    count = 4 # count [2,3,5,7]

    for i in primeList:
        add = True
        if not isDivin2or5(i): #easy div check for 2,3,5
            rot = i
            for j in range(len(str(i)) - 1):
                rot = 10 ** (len(str(i))-1) * (rot%10) + int((rot - rot%10)/10) #rotate the num
                if rot not in primeList:
                    add = False
                    break
            if add:
                count += 1
    print(count)


if __name__ == "__main__":
    main()

