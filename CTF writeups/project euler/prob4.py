biggestPal = 0

def isPali(n):
    return str(n) == str(n)[::-1]

""" my solution:
for i in range(100,1000):
    j = i
    while j<=999:
        if (i%10 != 0) and (j%10 != 0): #in these one of the 3dig numbers end with a zero
            cur =i*j
            if isPali(cur): #check for pali
                if cur > biggestPal:
                    biggestPal = cur
        j+=1

print(biggestPal)
"""
 
#see explanation in the website
for i in range(999,100,-1):
    if i%11 == 0:
        j = 999
        dj = 1
    else:
        j = 990 #990 is the biggest multiple of eleven in the 3dig range
        dj = 11
    while j>=i:
        cur = i*j
        if cur <= biggestPal:
            break

        if isPali(cur):     
            biggestPal = cur
        j -= dj

print(biggestPal)