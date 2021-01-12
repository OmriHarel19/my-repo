
def loadData(path):
    with open(path, 'r') as file:
        data = file.read()
    return data.replace("\n","")

def find_maxProd(data):
    prod = 0
    i = 0
    while i < (len(data)-13):
        temp = 1
        adj = data[i:i+13]
        if '0' in adj:          #means the prod of this seq is going to be 0
            i += adj.rfind('0')+1
        else:
            for j in adj:
                temp *= int(j)
            if temp > prod:
                prod = temp
            i+=1
    return prod


def main():
    data = loadData("C:/Users/עמרי/Desktop/project_euler/num_prob8.txt")
    print(data)
    print(find_maxProd(data))


if __name__ == "__main__":
    main()