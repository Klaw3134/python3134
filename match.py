# uso y explicxación de match
# def suma():
#     n1=int(input("ingrese un numero: "))
#     n2=int(input("ingrese otro numero: "))
#     print("el resultado de la suma es ",  n1+n2)

# def resta():
    # n1=int(input("ingrese un numero: "))
    # n2=int(input("ingrese otro numero: "))
    # print("el resultado de la resta es ",  n1-n2)    

# def multiplicacion():
#     n1=int(input("ingrese un numero: "))
#     n2=int(input("ingrese otro numero: "))
#     print("el resultado de la multiplicacion es ",  n1*n2)  

# def division():
#     try:
#             n1=int(input("ingrese un numero: "))
#             n2=int(input("ingrese otro numero: "))
#             print("el resultado de la division es ",  n1/n2)  
#     except ZeroDivisionError:
#          print(f"se produjo una excepcion")
    
# suma()


# def calcu():
       
#     while True:
#      try:
#          print ('''
#             1.- suma 
#             2.- resta 
#             3.- multiplicacion
#             4.- division
#             5.- salir   

#                 ''')



#         op=int(input("seleccione una opcion"))
#         match op:
#                 case 1:
#                     print("suma")
#                     suma()
#                 case 2:
#                     print("resta")
#                     resta()
#                 case 3:
#                     print("multiplicacion")
#                     multiplicacion()   
#                 case 4:
#                     print("division")
#                     division()
#                 case 5:
#                     print("saliendo") 
#                     break    
#                 case _:
#                  print("opcion invalida")
#         except ValueError:


# calcu()              


#crear un menu de carrito con las siguientes opciones
#1.- ingresar nombre del usuario
#será mostrado en la boleta, con un saludo
#2.-comprar, poner productos para poder comprar
#con su precio correspondiente ej: producto $1000
#3.- sacar boleta, calcular el precio neto
#y el precio más iva. mostrar totales
#bonus, mostrar cant de articulos que lleva
#4.-Salir
#consideraciones:
#por lo menos 3 productos
#no hay limite de compra
#se puede salir en cualquier momento
#los montos de lños productos son fijos


vodka=0
gin=0
vino=0
total=0
nom=input(print("Cual es su nombre?"))
print(f"Hola Bienvenid@, {nom}")
while True:
    print(''' productos disponibles
        1.-vodka $10000
        2.-Gin $15000
        3.-vino $8000
        4.-Salir

    ''')
    op=int(input("Selecciona lo que quieres llevar"))
    match op:
        case 1:
            print("usted lleva vodka")
            total+=10000
            vodka+=1
    
        case 2:
            print("llevas gin")
            total+=15000
            gin+=1
        
        case 3:
            print("ud lleva vinito")
            total+=8000
            vino+=1
        case 4:
            print("saliendo")
            break
        case _:
            print("Seleccione una opcion valida")
    print("usted lleva", "vodka",  vodka, "gin",  gin,"vino",  vino)
    print("el total neto es", total)  
    print("el total con IVA es", total*1.19) 
    