# productos=["shampoo", "jabon", "galleta"]
# precios=[3500, 2000, 4000]
# carrito=[]

# while True:
#     while True:
#         try:
#              print('''Seleccione una opcion
#                     1.- Agregar productos 
#                     2.- comprar 
#                     3.- crear boleta
#                     4.- Salir
#                             ''')
#              op=int(input("Seleccione opcion"))
#              break
#         except Exception:
#             print("")    
#             match op:
#                 case 1:
#                     prod=input("ingrese un producto")
#                     productos.append(prod)
#                     pre=int(input("ingrese el precio: "))
#                     precios.append(pre)
#                 case 2:
#                     for i in range (len(productos)):
#                         print(i+1, productos[i], "$", precios[i] )
#                     producto=int(input("Seleccione una opcion"))
#                     carrito.append(producto-1)
#                     print(carrito)
#                 case 3:
#                     total=0
#                     print("***********0*********")
#                     print("Articulos de limpieza ")
#                     for i in (carrito):
#                         print(productos[i], "$", precios[i])
#                         total=total+precios[i]
#                     print("la cantidad de articulo que lleva es" (len(carrito)))
#                     print("el total neto es", total)
#                     print("el total más IVA es", total*1.19)
#                 case 4:
#                     print("")
#                 case _:
#                     print("")  
# 
#   

# frutas={
#     "manzana": 1200,
#     "kiwi": 1500,
#     "platano": 1500,
# }


# while True:
#     try:
#         print('''
#         1.- ingresar fruta
#         2.- Mostrar fruta
#         3.- Actualizar Precio
#         4.- Eliminar Fruta            
#         5.- salir            
#             ''')
#         op=int(input("seleccione una opcion"))
#         match op:
#             case 1:
#                 fruta=input("ingrese el nombre de la fruta")
#                 precio=int(input("ingrese precio"))
#                 frutas[fruta]=precio

#             case 2:
#                 for key,dato in frutas.items():
#                     print(key,"$", dato )
#             case 3:
#                 for key,dato in frutas.items():
#                     print(key,"$", dato )
#                 fruta=input("Cual es el articulo cuyo precio deseas cambiar")
#                 if fruta in frutas:
#                     precio=int(input("ingrese el precio nuevo: "))
#                     frutas[fruta]=precio
#                 else:
#                     print("el articulo no existe")       

#             case 4:
#                 for key,dato in frutas.items():
#                     print(key, "$", dato)
#                     borrar=input("Qué aeticulo deseas eliminar?")
#                     del frutas[borrar]
#                     print(f"el articulo {borrar} fue borrado")
#             case 5:
#                 print("saliuendo")
#                 break    
#     except Exception as e:
#         print("el error es", e )


# import random

# def clave():
#     clave=3344
#     password=int(input("Ingrese su pass :"))
#     while clave!=password:
#         print ("ERORR, clave invalida")
#         password=int(input("Ingrese su pass :"))

#     print("Bienvenido al sistema")

# def ruleta():
#     barril=random.randint(1,6)
#     rul=int(input("Dispare"))

#     while rul!=barril:
#         rul=int(input("Dispare"))
#     print("BANG!!!")


# def suma():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(n1+n2)

# def suma_arg(n1,n2):
#     print(n1+n2) 



# def suma_ret():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     return n1+n2

# def suma_ret_arg(n1,n2):
#     return n1+n2

# suma() 
# suma_arg()
# print(suma_ret()*3)
# print(suma_ret_arg(9,8))


# def suma_1000(num):
#     return num+1000

# result=suma_1000(4000)
# print(result)


# def iva(num):
#     return num*1.19
# result=iva(5000)
# print(result)


4000
dsct 20%

800
3200
def desc(precio,desc):
     return precio-(precio*desc/100)


productos=[
     {"nombre": "lapiz", "precio": 400}, #0
     {"nombre": "estuche", "precio": 1000}, #1
     {"nombre": "goma", "precio": 200} #2
]

print(productos[0]["precio"])
print(productos)
nombre=input("nombre del producto")
precio=int(input("precio del producto"))
productos.append({"nombre": nombre, "precio": precio})
print(productos)


###### agregar art
#borrar
#actualizar
#mostrar listado
#salir