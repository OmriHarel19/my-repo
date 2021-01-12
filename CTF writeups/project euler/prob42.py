import math
from string import ascii_uppercase #because all the words in the file are uppercased

def loadData(path):
    with open(path, 'r') as file:
        data = file.read()
    data = data.replace("\"",'').split(",")
    return data

def wordSum(word):
    letters = [i for i in ascii_uppercase]
    sum = 0
    for i in word:
        sum += letters.index(i) + 1 #(because A is the 1st letter but its in position #0)
    return sum

def isTriNum(n):
    return math.sqrt(8*n+1).is_integer()

def triangle_name_count(data):
    count = 0
    for i in data:
        if isTriNum(wordSum(i)):
            count += 1
    return count

def main():
    data = loadData("C:/Users/עמרי/Desktop/project_euler/words_prob42.txt")
    print(data)
    print(triangle_name_count(data))


if __name__ == "__main__":
    main()