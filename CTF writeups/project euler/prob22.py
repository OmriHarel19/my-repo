
from string import ascii_uppercase #because all the words in the file are uppercased

def loadData(path):
    with open(path, 'r') as file:
        data = file.read()
    data = data.replace("\"",'').split(",")
    return sorted(data)

def wordSum(word):
    letters = [i for i in ascii_uppercase]
    sum = 0
    for i in word:
        sum += letters.index(i) + 1 #(because A is the 1st letter but its in position #0)
    return sum

def nameScores(data):
    sum = 0
    for i in range(len(data)):
        sum += wordSum(data[i])*(i+1)
    return sum

def main():
    data = loadData("C:/Users/עמרי/Desktop/project_euler/names_prob22.txt")
    print(nameScores(data))


if __name__ == "__main__":
    main()