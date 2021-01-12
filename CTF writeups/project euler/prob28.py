
def spiralSum(n):
    if n == 1:
        return 1
    sum = 1
    for i in range(3,n+1,2):
        sum += 4*(i**2) - 6*(i-1)
    return sum

def main():
    print(spiralSum(25))

if __name__ == "__main__":
    main()