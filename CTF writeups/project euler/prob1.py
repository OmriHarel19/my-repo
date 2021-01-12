#find the sum of all multiples of 3 and 5 between 0 and 1000

#computes the sum of the arithmetic progression using a1,an and d
def arithmeticSeqSum(first, last, n):
    return (int(first)+int(last))*(int(n)/2);

#the multiplies of the 3 and 5 are actualy arithmetic progressions
#the multiplies of 15 are the overlap between 3 and 5
sum3 = arithmeticSeqSum(3,999,333)
sum5 = arithmeticSeqSum(5,995,199)
sum15 = arithmeticSeqSum(15,990,66)

print(sum3)
print(sum5)
print(sum15)

print( "answer: " + str(sum3+sum5-sum15))