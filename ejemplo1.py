#ingresar dos numero 
a=int(input("Digite un numero: "))
b=int(input("Digite otro numero: "))
suma= a+b
multi=a*b
print("La suma de "+ str(a) + "y de "+ str(b) + "Es igual al: "+str (suma))
print("La multiplicacion de "+ str(a) + "y de "+ str(b) + "Es igual al: "+str (multi))

#Estrucutura de if
if(a>b):
    print("el numero" +str(a) + "es mayor que "+ str(b))
elif (a<b):
    print("el numero" +str(a) + "es mayor que "+ str(b))
else:
    print("Los numeros son iguales")