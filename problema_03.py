#dado el valor de venta de un producto, hallar el IGV (18%) y el precio de venta.

vv = float(input("Ingrese valor de venta: ")) 
igv = vv * 0.18
pv = vv + igv

print("El IGV es : ", igv)
print("El precio de venta es : " , pv)