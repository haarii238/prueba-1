producto= input ("¿Cuál es tu producto?:")
cantidad= int (input("Ingresa la cantidad:"))
IVA= cantidad * 0.16
total= cantidad+IVA
descuento= cantidad-0.5
print ("Resumen de su compra")
print ("Producto:", producto)
print ("precio: $", cantidad)
print ("IVA", IVA)
print ("total de la compra $",total)
if descuento>60:
    print ("Tienes descuento de 0.5")
    print ("precio con descuento $", descuento)
else:
    print ("no tienes descuento")