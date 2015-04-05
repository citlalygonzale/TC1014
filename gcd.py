def gcd(a,b):
    while b!=0:
        (a,b)=(b, a % b)
    return(a)
a=int(input( "Give me a number: "))
b=int (input ("Give me another number: "))
g= gcd(a,b)
print(g)
