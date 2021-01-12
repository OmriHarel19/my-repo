import math

def loadData(path):
    with open(path, 'r') as file:
        data = file.readlines()
    for line in range(len(data)):
        data[line] = list(map(int, data[line].replace("\n","").split(",")))
    return data

def maxExp(data):
    max = math.log(data[1][0])*data[1][1]
    index = 1
    cur = 0

    for i in range(2,len(data)-1):
        cur = math.log(data[i][0])*data[i][1]
        if cur > max:
            max = cur
            index = i

    return index+1 #add 1 because first line in list is 0 but in reality its 1

def main():
    data = loadData("C:/Users/עמרי/Desktop/project_euler/exponents_prob99.txt")
    print(data)
    print(maxExp(data))

if __name__ == "__main__":
    main()
