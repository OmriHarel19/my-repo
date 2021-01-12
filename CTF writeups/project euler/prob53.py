from math import comb

def comb_above1mill():
    count = 0 #represents the first comb above 1m that is givven in the question
    for i in range(23,101):
        mid = int(i/2)
        ncr = comb(i,mid)
        if ncr > 1000000:
            count += 1 + i%2 #if even: count += 1, if odd: count += 2

            mid -= 1
            ncr = comb(i, mid)
            while ncr > 1000000:
                count += 2
                mid -= 1
                ncr = comb(i,mid)

    return count


def main():
    print(comb_above1mill())

if __name__ == "__main__":
    main()
