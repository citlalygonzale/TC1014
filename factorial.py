#Este programa esta hecho para calcular el programa de un numero N

a='s'

while(a=='s'):
    num = int(input("Dame un numero: "))
    factorial = 1

    if num < 0:

        print("Sorry, el factorial no existe en numeros negativos")

    elif num == 0:

        print("El factorial de 0 es 1")

    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("El factorial de ",num,"es",factorial)
        a=input("Quieres intentar con otro numero? s/n  ")
