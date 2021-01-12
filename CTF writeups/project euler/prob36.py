
def isPali(x):
    return str(x) == str(x)[::-1]

def doubleBasePali(x):
    sum = 0
    for i in range(1,x,2): #checking only odd numbers because if x is even: bin(X) will end in '0' -> cant be palindrome
        if isPali(i) and isPali(bin(i)[2:]):
            print(i)
            sum += i

    return sum


def main():
    print(doubleBasePali(1000000))


if __name__ == "__main__":
    main()