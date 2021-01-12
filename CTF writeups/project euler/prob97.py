
def non_mersenne_prime():
    digits = 28433
    for i in range(7830457):
        digits = (digits*2)%(10**10)
    digits +=1
    return digits

def main():
    print(non_mersenne_prime())

if __name__ == "__main__":
    main()
