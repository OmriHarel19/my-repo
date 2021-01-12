import math

def isPenta(x):
    return (1 + math.sqrt(24*x+1)) % 6 == 0

def penta(n):
    return int(n*(3*n-1)/2)

def pentaJump(n): #returns the diff between P(n+1) - p(n)
    return 4 + 3*(n-1)

def minPentaDiff():
    i = 1
    while True:
        jump = pentaJump(i)
        if isPenta(jump) and isPenta(penta(i) - jump):
            return jump
        i += 1

def main():
    print(minPentaDiff())

if __name__ == "__main__":
    main()