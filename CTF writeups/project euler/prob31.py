
def coinSums(amount,options):
        #amount: current amount of money, options: of coins, setOfCoins: a set that collects all possibles sets of coins,
        #exit term: if amount = 0 means that this is a correct path
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        if options == []:
            return 0
        sum = 0
        #recursive call on all sub sums
        for i in range(len(options)):
            sum += coinSums(amount - options[i],options[0:i+1])

        return sum

def main():
   amount = 200
   options = [1,2,5,10,20,50,100,200]
   print(coinSums(amount,options))


if __name__ == "__main__":
    main()