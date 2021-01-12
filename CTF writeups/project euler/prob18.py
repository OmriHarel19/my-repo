import math

def strToArr(path):
    #getting the data from txt file
    with open(path, 'r') as file:
        data = file.read()
    #spliting to array by the new lines
    arr = data.split("\n")

    list = []


    for i in arr:
       values = i.split(" ")
       values = [int(j) for j in values]
       list.append(values)

    return list[::-1]

def maxPath(list):
    for i in range(1,len(list),1):
        for j in range(len(list[i])):
            list[i][j] = list[i][j] + max(list[i-1][j],list[i-1][j+1])
    list = list[::-1]
    print(list[0])

def main():
    print("this code also solves prob67")
    path = input("triangle file path:")
    maxPath(strToArr(path))

if __name__ == "__main__":
    main()