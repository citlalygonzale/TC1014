
def ad_sum(x,y):
    ans= x + y
    return ans

def ad_dif(x,y):
    ans= x - y
    return ans

def ad_div(x,y):
    ans= x / y
    return ans

def ad_mult(x,y):
    ans= x * y
    return ans

def ad_rem(x,y):
    ans= x % y
    return ans

# main program below
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))

print("The numbers you gave me are: ",a,"and",b)

s=ad_sum(a,b)
d=ad_dif(a,b)
dv=ad_div(a,b)
m=ad_mult(a,b)
r=ad_rem(a,b)

print("the sum of",a," and ",b,"is equals to: ",s)

print("the difference of",a," and ",b,"is equals to: ",d)

print("the division of",a,"and",b,"is equals to: ",dv)

print("the product of",a,"and",b,"is equals to: ",m)

print("the remainder of",a," and ",b,"is equals to: ",r)
