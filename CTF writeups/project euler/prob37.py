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

def is_Truncatable_prime(x):
    if x < 10 or (not isPrime(x)):
        return False

    #check if x has one or nine in edges, ex: 145 , 231,973,
    if x%10 == 1 or x%10 == 9 or int(str(x)[::-1])%10 == 1 or int(str(x)[::-1])%10 == 9:
        return False

    #check if any of the next digs appear in x
    digits = [0, 2, 4, 5, 6, 8]
    temp = x
    while temp > 0:
        if temp%10 in digits:
            return False
        temp = int(temp/10)

    #check if all primes slicing r->l:
    temp = x
    while temp > 10: #checking above 10 because if we reach 0<temp>10 it must be a prime (3,7 or 9)
        if not isPrime(int(temp/10)):
            return False
        temp = int(temp/10)

    ##check if all primes slicing l->r:
    temp = x
    while temp > 10:
        rot = temp%(10**(int(len(str(temp)))-1))
        if not isPrime(rot):
            return False
        temp = rot

    return True


def Truncatable_primes():
    sum = 0
    count = 0
    num = 31
    while count < 11:
        if int(str(num)[0]) == 3 or int(str(num)[0]) == 7:
            if num%10 == 3 or num%10 == 7:
                for i in range(1,len(str(num))-1,1):
                    if str(num)[i] not in ['1','3','7','9']:
                        break
                if isPrime(num) and is_Truncatable_prime(num):
                    print(num)
                    count += 1
                    sum += num
        else:
            if int(str(num)[0]) > 3 and int(str(num)[0]) < 7:
                num = 7 * (10 **(int(len(str(num)))-1)) + 1
            if int(str(num)[0]) > 7:
                num = 3 * (10**int(len(str(num)))) + 1
        num += 2
    return sum




def main():
    sum = Truncatable_primes()
    print(sum)


if __name__ == "__main__":
    main()