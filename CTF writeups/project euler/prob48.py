
def selfPowers(x):
    digits = 405071317
    for i in range(11,x+1):
        if i%10 != 0:
            digits += (i**i)%(10**10)
    return digits%(10**10)

def main():
    print(selfPowers(1000))

if __name__ == "__main__":
    main()
