def square_dig(n):
    sum = 0
    for i in str(n):
        sum += int(i)**2
    return sum

def square_dig_chain(n):
    goTo1 = [1,10,13,32,44]
    goTo89 = [89,85,145,42,20,4,16,37,58]
    temp = 0
    count = 0
    for i in range(1,n+1):
        print(i)
        temp = i
        chain = []
        while (temp not in goTo1) and (temp not in goTo89):
            chain.append(temp)
            temp = square_dig(temp)
        if temp in goTo89:
            goTo89 += chain
            count += 1
        else:
            goTo1 += chain

    return count



def main():
    print(square_dig_chain(1000000))

if __name__ == "__main__":
    main()
