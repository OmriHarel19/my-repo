import math

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

def maxDigSum(n):
    max = 0
    sum = 0
    for i in range(int(n/2),n):
        if i%10 != 0:
            for j in range(int(n/2),n):
                temp = sum_digits(i**j)
                if temp > max:
                    max = temp
    return max

def main():
    print(maxDigSum(100))

if __name__ == "__main__":
    main()

