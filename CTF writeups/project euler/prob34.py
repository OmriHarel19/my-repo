
def fact(x):
    if x == 0:
        return 1
    fact = 1
    for i in range(x,1,-1):
        fact *= i
    return fact

def sumDigFact(x,factorials): #using list of factorials of digits 0-9
    sum = 0
    while x > 0:
        sum += factorials[x%10]
        x = int(x/10)
    return sum

def main():
    factorials = []
    for i in range(10):
        factorials.append(fact(i))
    print(7*factorials[9] + 1)

    sum = 0
    for i in range(3,7*factorials[9] + 1,1):
    #this is the upper limit because above [7*fact(9) (corrasponds to 9999999)]
    # the number itself will be bigger than the sum of factorials of his digs
        if i == sumDigFact(i,factorials):
            sum += i

    print(sum)

if __name__ == "__main__":
    main()
