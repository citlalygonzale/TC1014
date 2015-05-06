fr=open("93cars.dat.txt","r")
mpg=0
mpgh=0
mprice=0
cars=0
f=1
for i in fr:
    if f%2==1:
        mpg=mpg+float(i[52:54])
        mpgh=mpgh+float(i[55:57])
        mprice=mprice+float(i[42:46])
        cars=cars+1
    f=f+1
a=round(mpg/cars,6)
b=round(mpgh/cars,6)
c=round(mprice/cars,6)

print("The average gas mileage in City MPG is: ", a)
print("The average gas mileage on Highway MPG is: ",b)
print('The average midrange price of the vehicles in the set is: ',c)
