# uso y ejemplos de numeross
#### controlF para remplazar palabras
        #    -4  -3  -2   -1
# numeros=[10, 5, 20, 45, ]
        #    0   1  2   3
# print(numeros [-1])
# numeros.reverse()
# for numero in numeros:
#     print("numero" , numero*3)

# numeros.append(64)    #(agrega un dato al final de la lista)


# frutas=["durazno", "naranja", "manzana", "pera"]


# for fruta in frutas:
#     print(fruta)
# apellidos=["navarrete", "canales", "gonzalez"]
# nombres=["claudia", "erika", "cata"]
# while True:
#     print('''  
#            1.- Ingresa un nombre y apellido
#           2.- buscar nombres
#           3.- mostrar nombres y apellidos
#           4.- salir 
#           ''')
#     op=int(input("seleccione una opcion"))
#     match op:
#         case 1:
#             p1=input("ingrese un nombre")
#             p2=input("ingrese un apellido")
#             nombres.append(p1)
#             apellidos.append(p2)
            
#         case 2:
#             nom=input("buscar nombre")
#             if nom in nombres:
#                 print("se encontró nombre")
#             else:
#                 print("no existe")    
            
#         case 3:
#             # nomb=0
#             # for n in nombres:
#             #     print(nombres[nomb], apellidos[nomb])
#             #     nomb+=1
#             for i in range(len[nombres]):
#                 print(nombres[i], apellidos[i])


#         case 4:  
#             print("salir")
#             break
#         case _:
#             print("")      

###### Seleccione una opcion
# 1.- Agregar productos (nombre del producto y precio)
# 2.- comprar (submenu mostrando productos y precios)
# 3.- crear boleta
# 4.- Salir


productos=["shampoo", "jabon", "galleta"]
precios=[3500, 2000, 4000]
carrito=[]

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
                        for i in range(len(productos)):
                                print(productos[i], precios[i])
                case 4:
                        print("")
                case _:
                        print("")    
                        
          
 



