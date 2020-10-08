veces=int(input("Ingrese numeros: "))
impar=0
par=0
for i in range(veces):
	numeros=int(input("Ingrese numeros: "))
	if numeros%2==0:
		par=par+1
	elif numeros%2!=0:
		impar=impar+1
print("Numeros pares: "+str(par))
print("Numeros impares: "+str(impar))
