import time

def isIncreasing(n):
    n = str(n)
    for i in range(len(n) - 1):
        if int(n[i + 1]) < int(n[i]):
            return False
    return True

def isDecreasing(n):
    n_rev = str(n)[::-1]
    for i in range(len(n_rev) - 1):
        if int(n_rev[i + 1]) < int(n_rev[i]):
            return False
    return True

def isBouncy(n):
    return (not isIncreasing(n)) and (not isDecreasing(n))

def bouncy_precent():
    bouncy = 19602
    total = 21780
    while bouncy/total < 0.99:
        total += 1
        if isBouncy(total):
            bouncy += 1
        print(bouncy/total)
    return total

def main():
    s_time = time.time()
    print(bouncy_precent())
    t = time.time() - s_time
    print(t, "seconds")

if __name__ == "__main__":
    main()

