from functools import reduce

def loadData(path):
    with open(path, 'r') as file:
        data = file.readlines()
    for line in range(len(data)):
        data[line] = list(map(int, data[line].replace("\n","").split(" ")))
    return data

def maxProd(grid):
    maxProd = 1
    prod = 1
    for i in range(len(grid)-3):
        products = []
        for j in range(len(grid) - 3):
            products.append(reduce(lambda x, y: x*y,[grid[i][k] for k in range(j,j+4)])) #add right
            products.append(reduce(lambda x, y: x*y,[grid[k][j] for k in range(i,i+4)])) #add bottom
            products.append(reduce(lambda x, y: x*y,[grid[i+k][j+k] for k in range(4)])) #add right down diag
            if j > 2:
                products.append(reduce(lambda x, y: x * y,[grid[i+k][j-k] for k in range(4)])) #add left down diag
            prod = max(products) #find the max of current products
            if prod > maxProd:
                maxProd = prod #update

    return maxProd

def main():
    grid = loadData("C:/Users/עמרי/Desktop/project_euler/grid_prob11.txt")
    print(grid)
    print(maxProd(grid))

if __name__ == "__main__":
    main()
