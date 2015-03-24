print ("Citlali Gonzalez")

def triangles(size):
    for i in range(1, size +1):
        for c in range(i):
            print("T", end="")
        print()

    for i in range(1,size):
        for c in range(size-i):
            print("T", end="")
        print()

size=int(input("Give me the size of the triangle: "))
x=triangles(size)
