
def loadData(path):
    with open(path, 'r') as file:
        data = file.readlines()
    for line in range(len(data)):
        data[line] = list(map(int, data[line].replace("\n","").split(",")))
    return data
'''
def towPathSum(data):
    #calc last line & row:
    for i in range(len(data)-2,-1,-1):
        data[-1][i] += data[-1][i+1]
        data[i][-1] += data[i+1][-1]
    #calc all of the matrix:
    for i in range(len(data)-2,-1,-1):
        for j in range(i, -1, -1):
            data[i][j] += min(data[i][j+1],data[i+1][j])
            if i != j:
                data[j][i] += min(data[j+1][i],data[j][i+1])

    return data[0][0]
'''

def main():
    '''
    data = loadData("C:/Users/עמרי/Desktop/project_euler/matrix.txt")
    print(data)
    print(twoPathSum(data))

    data = [
            [131,673,234,103,18],
            [201,96,342,965,150],
            [630,803,746,422,111],
            [537,699,497,121,956],
            [805,732,524,37,331]
            ]
    print(data)
    twoPathSum(data,0,0)
    print(data[0][0])
    '''

if __name__ == "__main__":
    main()

