#find the sum of all even fibonachi terms that are smaller than 4 million

limit = 4000000
sum = 0
a = 1
b= 1
c = a+b

while c<limit:
    sum += c
    a = b+c #f(n+1)
    b = c+a #f(n+2)
    c = a+b #f(n+3)

print(sum)