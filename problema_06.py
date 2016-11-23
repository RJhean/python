# Dado un número de 5 dígitos, devolver el número en orden inverso

n = int(input("Ingrese un número de 5 dígitos : "))
ni = 0
resultado = 0

resultado = n % 10
n = int(n/10)
ni = resultado*10


resultado = n % 10
n = int(n / 10)
ni = (ni+resultado) * 10


resultado = n % 10
n = int(n  / 10)
ni = (ni + resultado )*10


resultado = n % 10
n = int(n/10)
ni = (ni+resultado)*10


ni = ni + n 
print(ni)