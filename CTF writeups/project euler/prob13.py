

def calcSum():
    grid = open('C:/Users/עמרי/Desktop/grid.txt', 'r')
    data = grid.read().split("\n")

    sum = 0
    for i in data:
        sum += int(i[0:11])
    return str(sum)[0:10]


def main():
    print(calcSum())


if __name__ == "__main__":
    main()
