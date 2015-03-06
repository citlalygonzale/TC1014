import statistics

def tot_s (c):
    t=0
    #add to total each value in t
    for indice in range(len(c)):
        t= t + c[indice]
    return t

def ave_s (c):
    av = mitot / 10
    return av

def stand_s (c):
    st= statistics.stdev(l)
    return st

l=[]

x=0

while(x < 10):
    x=x+1
    n=int(input("Enter a number: "))
    l.append(n)

    mitot= tot_s(l)
    prom =ave_s (l)
stand= stand_s (l)

print(mitot)
print (prom)
print (stand)
