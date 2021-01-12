# find the biggest prime divider of a given num

def findNextPrime(list): #list min is: [2,3]
    loopBool = False
    primeBool = True

    i = list[-1]+2 #beginning from the last prime in the list
    while loopBool == False:
        primeBool = True
        for j in list:
            if i % j == 0: #means i is not prime
                primeBool = False
                break
        if primeBool: #if we got here i is a prime
            list.append(i)
            loopBool = True
        i += 1
    return list

num = 600851475143
list = [2,3]
primeDividorsList = []
addNextPrime = True
stopMidLoop = True
maxPrime = 1

num2 = 1245

while num > 1:
    addNextPrime = True
    stopMidLoop = True
    for j in list :
        if stopMidLoop:
            if num % j ==0:
                num = num/j;
                addNextPrime = False
                stopMidLoop = False
    list = findNextPrime(list)

print(list[-2])

"""
for i in range(10000):
    list = findNextPrime(list)
print(list)
"""



