
def s(n):
    numOfnines = int(n/9)
    if numOfnines >= 10:
        return 999999936 #val of ('9'*10)%1,000,000,007
    if numOfnines == 9:
        return 999999999 - 7*(n%9) #val of ([1..8]('9'*10))%1,000,000,007

    return int(str(n%9)+'9'*int(n/9))

def S_original(k):
    sum = 0
    for n in range(1,k+1):
        sum += s(n)
        if sum > 1000000007:
            sum = sum%1000000007
    return sum

def S(low,high,last):
    mod_const = 1000000007
    sum = last
    for n in range(low,high+1):
        sum += s(n)
        if sum > mod_const:
            sum = sum % mod_const
    return sum

def next_S(S,n):
    if S == 0:
        return 1
    return S + s(n+1)

def fibo(n,lst):
    if n == 0 or n == 1:
        return lst[n]
    lst.append(lst[-1]+lst[-2])
    return lst[-1]

def main():

    modulu = 1000000007
    lst = [0,1]
    sum = 0
    #last_S = 0
    low = 1
    for i in range(2,91):
        fibo_val = fibo(i,lst)
        print("i", i, "fib(i)", fibo_val)
        if low >= 90:
            sum += 999999936*(fibo_val-low+1)
            sum = sum%modulu
        else:
            sum += S(low,fibo_val,sum)
        print("sum",sum)
        low = fibo_val + 1

    print("done",sum)
    '''
    for i in range(1,11):
        print(S_original(i))
    '''

if __name__ == "__main__":
    main()

