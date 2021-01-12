import math

def pitag():
    for i in range(1,1000):
        for j in range(1,1000):
            if(i + j + math.sqrt(i**2 + j**2) == 1000.0):
                print(i,j,math.sqrt(i**2 + j**2))
                return(i*j*math.sqrt(i**2 + j**2))
    print("done")

print(pitag())