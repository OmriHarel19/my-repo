import math

def cancellingFrac():
    final_frac = 1
    for i in range(11,50,1):
        for j in range(i+1,100,1):
            if i%10 != 0 and j%10 != 0:
                if (i%10) == (int(j/10)) and i/j == int(i/10)/(j%10):
                    print(i,j,i/j)
                    final_frac *= i/j
    print(round(final_frac ** (-1)))


def main():
    cancellingFrac()

if __name__ == "__main__":
    main()