
def pow5digsum(x):
    sum = 0
    while x > 0:
        sum += (x%10)**5
        x = int(x/10)
    return sum

def main():

    sum = 0
    for i in range(6*(9**5)+1): #upper lim same as explaination in prob34
        if i == pow5digsum(i):
            sum += i
            print(i)
    print(sum-1) #sub one cuz its not in the sum

if __name__ == "__main__":
    main()
