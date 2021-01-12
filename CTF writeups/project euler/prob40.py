
def Champernowne_const():
    dig_place = 1
    step = 1
    cur_place = 1
    prod = 1
    i = 1
    while dig_place <= 1000000: #running until millionth dig
        if len(str(i)) > len(str(i-1)): #ex: i = 100, step = 2 -> step = 3 (cuz len(i) is now 3
            step += 1
        if cur_place <= dig_place < cur_place + step: #if the dig in the "dig_place" is one of i's digits
            for j in range(step): #run on i's digits
                if cur_place + j == dig_place:
                    prod *= int(str(i)[j]) #update prod
                    dig_place *= 10 #update to next dig place
        i += 1
        cur_place += step

    return prod

def main():
    print(Champernowne_const())


if __name__ == "__main__":
    main()