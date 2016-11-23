# Hallar la potencia de a^n, donde a y n pertenecen a Z+ (Números enteros positivos)

a = int(input("Ingrese el número base : "))
n = int(input("Ingrese el exponente : "))

#resultado = a**n
resultado = pow(a,n)
print("El resultado de la potencia es :" ,resultado)