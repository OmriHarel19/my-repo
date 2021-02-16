def calcCheckSum(num):
    div = 97
    num = int(num + "00")
    reminder = num % div
    return (div + 1) - reminder


number = input("Enter a num:")
print(f"this is num: {number}")

print(f"check sum of {number} is: {calcCheckSum(number)}")


