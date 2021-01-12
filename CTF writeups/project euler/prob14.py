
def  collatz_seq_num(n): #returns the number steps until n reaches to 1
    count = 0
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count += 1
    return count

def longest_collatz_seq(n): #returns the number from 1 up to n that provides the biggest  collatz_seq_num(n)
    if n<3:
        return

    num = n-1
    count = collatz_seq_num(n-1)

    for i in range(n-2,1,-1):
        temp = collatz_seq_num(i)
        if temp > count:
            count = temp
            num = i
    return num



def main():
    print(longest_collatz_seq(1000000))




if __name__ == "__main__":
    main()
