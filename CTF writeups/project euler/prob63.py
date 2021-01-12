
def powerfulNumCount():
    count = 0
    for i in range(1,10,1): #10 is the upper lim because 10**1 = 10 = len of 2 > 1
        pow = 1
        while len(str(i**pow)) == pow:
            print(i,pow,i**pow)
            count += 1
            pow += 1
    print(count)

def main():
    powerfulNumCount()

if __name__ == "__main__":
    main()