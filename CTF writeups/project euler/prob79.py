
def loadData(path):
    with open(path, 'r') as file:
        data = file.read()
    return data.split("\n")

def main():
    print(set(loadData("C:/Users/עמרי/Desktop/project_euler/keylog_prob79.txt")))
    ##solution: 73162890 -> made with pen and paper

if __name__ == "__main__":
    main()