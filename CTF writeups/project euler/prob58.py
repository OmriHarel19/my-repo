import math

def isPrime(x):
    if x == 1 or x == 0:
        return False
    if x in [2,3,5,7]:
        return True
    if x%2 == 0:
        return False
    for i in range(3,int(math.sqrt(x))+1, 2):
        if x%i == 0:
            return False
    return True

def spiralPrimes():
    primes = 8
    total = 13
    len = 7
    while (primes/total) >= 0.1:
        len += 2
        for i in range(1,4):
            diag = len**2 - i*(len-1)
            if isPrime(diag):
                primes += 1
        total += 4
        print(primes/total)


    return len


def main():
    print(spiralPrimes())

if __name__ == "__main__":
    main()
