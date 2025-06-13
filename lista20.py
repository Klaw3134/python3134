productos=["shampoo", "jabon", "galleta"]
precios=[3500, 2000, 4000]
carrito=[]

while True:
    while True:
        try:
             print('''Seleccione una opcion
                    1.- Agregar productos 
                    2.- comprar 
                    3.- crear boleta
                    4.- Salir
                            ''')
             op=int(input("Seleccione opcion"))
             break
        except Exception:
            print("")    
            match op:
                case 1:
                    prod=input("ingrese un producto")
                    productos.append(prod)
                    pre=int(input("ingrese el precio: "))
                    precios.append(pre)
                case 2:
                    for i in range (len(productos)):
                        print(i+1, productos[i], "$", precios[i] )
                    producto=int(input("Seleccione una opcion"))
                    carrito.append(producto-1)
                    print(carrito)
                case 3:
                    total=0
                    print("***********0*********")
                    print("Articulos de limpieza ")
                    for i in (carrito):
                        print(productos[i], "$", precios[i])
                        total=total+precios[i]
                    print("la cantidad de articulo que lleva es" (len(carrito)))
                    print("el total neto es", total)
                    print("el total más IVA es", total*1.19)
                case 4:
                    print("")
                case _:
                    print("")    
                        
          