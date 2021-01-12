
def countLetters():#(of all written numbers from 1 to 1000 included)
    # dictionary: keys == worrds of the needed numbers, values: number of letters for each word
    dic = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3
        , 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
           20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8, "and": 3}

    count = 0

    # adding the letters of all the appearnces of [1..9]
    sumLetters1to9 = sum([dic[i] for i in range(1, 10, 1)])
    print("1->9:")
    print(sumLetters1to9)
    count +=  sumLetters1to9

    # adding the letters of all the appearnces of [11..19]
    sumLetters10to19 = sum([dic[i] for i in range(10, 20, 1)])
    print("11->19:")
    print(sumLetters10to19)
    count += sumLetters10to19  # this sum appears only once in each hundred

    # adding the letters of all the appearnces of [20..99]
    sumLetters20to90 = sum([dic[i] for i in range(20, 100, 10)])
    print("20->:99")
    print(10 * sumLetters20to90  + 8 * sumLetters1to9)
    count +=  10 * sumLetters20to90  + 8 * sumLetters1to9# 9: times that sumLeters1to9 is in each hundred
    sumLetters1to99 = count
    print("1->99:")
    print(sumLetters1to99)

    #100-999:
    #adding all 1-9 which are prefixes for the hundreds:
    print("1->9 prefixes:")
    print(sumLetters1to9 * 100)
    count += sumLetters1to9 * 100

    #adding all 1-99:
    print("all 1->99:")
    print(9*sumLetters1to99)
    count += 9*sumLetters1to99

    # adding all the single "hundreds"
    print("all single hundreds:")
    print(9 * dic[100])
    count += 9 * dic[100]

    # adding the letters of all the appearnces of "hundred and"
    print("all 'hundred and':")
    print(891 * (dic[100]+dic["and"]))
    count += 891 * (dic[100]+dic["and"]) #(1000 - 100) = 900 - 9(single hundreds) = 891

    print("adding '1000':")
    count += dic[1000] + dic[1]  # adding to sum the num letters of (1000)

    print("tatal is:")
    print(count)


def main():
    countLetters()

if __name__ == "__main__":
    main()