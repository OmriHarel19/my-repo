
def create_pandigital(digits,dividors,num_str):
    #digits - list of remaining digits to create a pandigital
    #dividors - list of remaining dividors to create a pandigital
    #num_str - the current num in type string (this we can save the needed zero in its place)
    if dividors == []: #means that that num is correct
        return int((digits[0]*(10**int(len(num_str)) + int(num_str))))
    sum = 0
    for i in range(len(digits)):
       if (digits[i] * 100 + int(num_str[0:2])) % dividors[-1] == 0:
            sum += create_pandigital(digits.remove(digits[i]),dividors.pop(),str(digits[i])+num_str)
    return sum



def Sub_string_divisibility():
    mults = [i for i in range(round(100/17)*17,1000,17)]
    sum = 0
    for i in mults:
        if len(str(i)) == len(set(str(i))):
            sum += create_pandigital
    return sum



def main():

    num_str = "289"
    dividors = [2,3,5,7,11,13]
    digits = [0,1,3,4,5,6,7]
    print(create_pandigital(digits,dividors,num_str))
'''
'''

if __name__ == "__main__":
    main()