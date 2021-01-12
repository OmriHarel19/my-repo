import math

''' recursive alg
def converge(iterations): #only calc the fraction part of the vonverge, so need to remember to add one at the end
    if iterations == 1:
        return 1,2
    numerator, denominator = converge(iterations-1)
    return denominator,(2*denominator + numerator)

def square_root2(iterations):
    numerator, denominator = converge(iterations)
    return numerator+denominator,denominator
'''

def converge(numerator, denominator): #returns the numerator, denominator of the "next" converge
    if numerator == 0 and denominator == 0:
        return 3,2
    return 2*denominator + numerator,denominator + numerator

def square_root2_estimate(iterations): # check for every current estimation if numerator has more digits then denominator
    numerator = 0
    denominator = 0
    count = 0
    for i in range(1, iterations+1):
        numerator, denominator = converge(numerator, denominator)
        if int(math.log10(numerator)) > int(math.log10(denominator)): #int(log10(num)) -> return the numbers of digits of num
            count += 1
    return count

def main():
    iters = 1000
    count = square_root2_estimate(iters)
    print(iters,"iter:",count)

if __name__ == "__main__":
    main()
