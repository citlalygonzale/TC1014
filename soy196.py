print("Citlali Gonzalez")

def inv(low):
    low=str(low)
    low=low[::-1]
    low=int(low)
    return(low)

numran=[]
lychrel=[]

low=int(input("Give me the lower bound: "))
up=int(input("Give me the upper bound: "))

for i in range (up-low+1):
    numran.append(low)
    low=low+1

palindromes=0
nolychrel=0
candidates=0

for i in numran:
    flip=inv(i)
    if i==flip:
        palindromes=palindromes+1
    else:
        ite1=flip+i
        ite2=inv(ite1)
        for i1 in range(30):
            if ite1==ite2:
                nolychrel=nolychrel+1
                break
            else:
                ite1=ite1+ite2
                ite2=inv(ite1)
                if (i1==29):
                    candidates=candidates+1
                    lychrel.append(i)

print("There are",palindromes,"palindromes" )
print("There are",nolychrel,"nolychrel")
print("There are",candidates,"numbers that are no candidates")

if candidates!=0:
    print("The lychrel numbers are: ",lychrel)
