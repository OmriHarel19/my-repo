import math

def isPenta(x):
    return (1 + math.sqrt(24*x+1)) % 6 == 0

def hexNum(idx):
    return 2*(idx**2) - idx

def find(place): #finds the next num after n(40755) which is triangular,pentagonal and hexagonal
    while True:
        hex = hexNum(place)
        if isPenta(hex):
            return hex
        place += 1

#conclusion: every hexagonal num is also triangle num: the hexagonals are the triangles in the odd indexes (except 1 at the beginning)

def main():
    print(find(144))

if __name__ == "__main__":
    main()