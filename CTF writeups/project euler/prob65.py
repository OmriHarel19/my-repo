
def sum_digits(n):
   sum = 0
   while n:
       sum, n = sum + n % 10, n // 10
   return sum

def converge(iteration):
    numerator,denominator = 3,1
    lastNum,lastDen = 2,1
    tempNum, tempDen = lastNum,lastDen
    multof2 = 2
    for i in range(3,iteration+1):
        if i%3 == 0:
            lastNum,numerator = numerator,multof2*numerator+tempNum
            lastDen,denominator = denominator,multof2*denominator+tempDen
            tempNum,tempDen = lastNum,lastDen
            multof2 += 2
        else:
            lastNum,numerator = numerator,numerator+tempNum
            lastDen,denominator = denominator,denominator+tempDen
            tempNum, tempDen = lastNum, lastDen
    return numerator



def main():
    conv = converge(100)
    print(conv)
    print(sum_digits(conv))

if __name__ == "__main__":
    main()