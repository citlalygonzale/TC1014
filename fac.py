a='y'

while(a=='y'):

    def fact(m):
        n = m
        y = 1
        while (n > 1):
            y = y * n
            n = n - 1
        return (y)

    m = int ( input ("Give me a number: "))
    f = fact(m)
    print ("The factorial of the number ",m, "= ",f)

    a = input ("Do ou want to try again the program ? y/n : ")
print (" Thanks ")
