#Hallar la raiz de un numero entero, en donde a y n pertenecen a Z+ (números enteros positivos)

a = int(input("Ingrese el radicando : "))
n = int(input("Ingrese el ìndice de la raiz : "))

resultado = int(pow(a,(1/n)))

print("La raiz de ", a , " es : " ,resultado)