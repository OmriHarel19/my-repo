
import math

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

#see solution in website 




