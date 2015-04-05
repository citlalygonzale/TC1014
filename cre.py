def babylon(rt):
    b=rt
    cont=1
    guess=b/2
    if(rt==0):
    	print (rt)
    elif(rt<0):
    	print("The root can't be negative")
    else:
        a=rt/guess
        ave=(a+guess)/2
        guess=ave
        cont=cont+1
    return guess
num=float(input("Give me a number: "))
by= (babylon(num))
print ("The babylonian root of ",num, "=", by)
