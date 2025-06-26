# # ejemplo de carrito con categorias-+
# total=0
# cantart=0
# while True:
#     try:
#         op=int(input('''
#              Seleccione una opcion con un numero entero
#                      1.- Comprar verduras
#                      2.- Comprar frutas
#                      3.- Pagar
#                      4.- Salir
#                      '''))
        
#         match op:
#             case 1:
#                 while True:
#                     try:
#                         op=int(input('''
#                                      Seleccione una opcion con un numero enterro
#                                      1.- Frutilla $1500
#                                      2.- Pera $1200
#                                      3.- Manzana $1300
#                                      4.- volver al menu principal

#                                     ''' ))
                        
#                         match op:
#                             case 1:
#                                 print("Has seleccionado frutilla")
#                                 total+=1500
#                                 cantart+=1
#                             case 2:
#                                 print("Has seleccionado Pera")
#                                 total+=1200
#                                 cantart+=1
#                             case 3:
#                                 print("has seleccionado Manzana")
#                                 total+=1300
#                                 cantart+=1
#                             case 4:
#                                 print("Volviendo...")
#                                 break
#                             case _:
#                                 print("Opcion invalida")
#                     except Exception:
#                          print("Solo puede ingresar numeros enteros")
#                     print("Tu total hasta ahora es", total)    
#             case 2:
#                 while True:
#                     try:
#                         op=int(input('''
#                                      seleccione una opcion con un numero entero
#                                      1.- papa $1500
#                                      2.- Lechuga $1200
#                                      3.- cebolla $1300
#                                      4.- volver almenu principal

#                                      '''))     

#                         match op:

#                             case 1:
#                                 print("has seleccionado papa")
#                                 cant=int(input("cuantas papas llevará?"))
#                                 total+=cant*1500
#                                 cantart+=cant
#                             case 2:
#                                 print("Has seleccionado lechuga")
#                                 total+=1200
#                                 cantart+=1
#                             case 3:
#                                 print("Has seleccionado Cebolla")
#                                 total+=1300
#                                 cantart+=1
#                             case 4:
#                                 print("volviendo...")
#                                 break
#                             case _:
#                                 print("opcion invalida")
#                     except Exception:
#                         print("Solo se pueden ingresar numeros enteros")
#                     print(" tu total hasta ahora es de", total)
#             case 3:
#                 print("Has seleccionado pagar")
#                 print(f"El total de articulos es de {cantart}")
#                 print(f"El total a pagar es {total}")
#                 print(f"El totala pagar más IVA es {round(total*1.19)}")
#             case 4:
#                 print("Saliendo...")
#                 break
#             case _:

#                 print("opcion invalida")
#     except Exception:
#         print("Solo puede ingresar numeros enteros")            
# 
##             
# ## Domingo de pascua ####
# Preguntar la Cantidad de niños que buscan huevitos de chocolates
# Cuando se termine la busqueda , preguntar cantos huevos encontró cada uno
# y clasificarlos de la siguiente forma
# Menos de una docena : NOOB
# Entre una docena a 24: Master
# 25 huevos o mas :Legend
# Mostrar resumen, y mostrar la mayor cantidad de huevitos encontrados por un solo niño

# import random
# while True:
#     try:
#         cantniños=int(input("Cuantos niños van a buscar Huevos?"))
#         while cantniños<0:
#             print("ERROR, solo ingrese numero positivos")
#             cantniños=int(input("Cuantos niños van a buscar huevos?"))

#         noob=0
#         master=0
#         legend=0
#         top=0
#         for n in range(cantniños):
#             canthuevos=random.randint(5,30)
#             if canthuevos>top:
#                 top=canthuevos

#             print(f"el niño numero{n+1} encontró {canthuevos}, huevos")
#             if canthuevos<12:
#                 noob+=1
#             elif canthuevos>=12 and canthuevos<=24:
#                 master+=1
#             else:
#                 legend+=1
#         print("la cantidad del grupo noob es", noob)                    
#         print("la cantidad del grupo master es", master)                    
#         print("la cantidad del grupo legend es", legend)                    
#         print("la mayor cantidad de huevos encontrada por un niño fue:" , top)
#         break
#     except Exception:
#         print("solo numeros enteros")                    

        
#### atletas  de salto alto
#### ingrese la cantidad de atletas que participarán
#cada atleta de be hacer un salto alto en el rango 1.55 mt y 3.78 mt
#los atletas bajo 1.55 no califican entre 1.56 y 2 bronce
#entre 2.1 y 3 plta
#3.1 y más adamantium

# import random
# bronce=0
# plata=0
# adamantium=0
# nocal=0
# salto=0
# record=0
# while True:
    
#         cantAtleta=int(input("Ingrese cantidad de atletas que participarán"))
#         while cantAtleta<0:
             
#             print("Ingrese sólo numeros enteros")
            
#             cantAtleta=int(input("ingrese cantidad de atleta que participarán"))
#         for A in range(cantAtleta):
#             salto=random.uniform(1.0, 3.78)
#             salto=round(2)
            
#             if salto>record:
#                  record=salto
                 
#             print(f"el atleta numero {A+1} saltó: {salto} metros") 

#             if salto<=1.55:
                
#                 nocal+=1
#             elif salto>=1.56 and salto<=2.0:
                
#                 bronce+=1
#             elif salto>=2.1 and salto<=3.0:
                
#                 plata+=1
#             else:
                 
#                  adamantium+=1
#             print("el record actual es", record)
#         print("No alcanzan a calificar:", nocal)                 
#         print("Ganan Bronce:", bronce)                 
#         print("Ganan Plata:", plata)                 
#         print("Ganan ADAMANTIUM:", adamantium)  
                      
       
 ### librería
 # crear menu de comics
 # 1.-comprar
 # 2.-generar boleta
 # 3.-salir
 # en la op de comprar mostrar los comiscs con sus precios
 # cuando se compra, mostrar la cantidad de articulos que lleva
 # mas el monto neto y monto con iva
 # si ingresa el cod de dscto "IAMBATMAN" 
 # obtiene 25% de descuento al valor neto

# total=0
# cantart=0
# cod="IAMBATMAN"
# while True:
#     try:
#         op=int(input(''' Seleccione una opción. Utilice numeros enteros
                     
#                      1.- Comprar
#                      2.- Generar boleta
#                      3.- Salir
#                      '''))

#         match op:
#             case 1:
#                 while True:
#                     try:
#                              op=int(input('''
#                                       Seleccione una opcion con un numero entero:
#                                       1.- comics 1 $2000
#                                       2.- comics 2 $3000
#                                       3.- comics 3 $2500
#                                       4.- salir

#                                      ''' ))
#                              match op:
#                                   case 1:
#                                        print("llevas el comics 1 $2000")
#                                        total+=2000
#                                        cantart+=1
#                                   case 2:
#                                        print("llevas el comics #2 $3000") 
#                                        total+=3000
#                                        cantart+=1
#                                   case 3:
#                                        print("llevas el comics #3 $2500")  
#                                        total+=2500
#                                        cantart+=1
#                                   case 4:
#                                        print("volviendo al menu...")
#                                        break
#                                   case _:
#                                        print("opcion invalida") 

                                           
#                     except Exception:
#                          print("Solo puede ingresar numeros enteros")
#                     print("Tu total hasta ahora es", total)  

#             case 2:
#                   while True:
#                        op=input("INgrese codigo de descuento")
#                        if op==cod:             




# total=0
# comp="soytoaku"
# producto=0
# pik=0
# otak=0
# pulpo=0
# ang=0
# while True:
#     try:
#         op=int(input("""Menu de sushi
#               1) Pikacu roll $4.500
#               2) otaku roll $5.000
#               3) pulpo venenoso roll $5.200
#               4) Anguila electrica roll $4.800
#               5) Terminar compra
#               """))
#         match op:
#             case 1:
#                 print("Handroll Pikacu roll agregado")
#                 total+=4500
#                 producto+=1
#                 pik+=1
#             case 2:
#                 print("Handroll otaku roll agregado")
#                 total+=5000
#                 producto+=1
#                 otak+=1
#             case 3:
#                 print("Handroll pulpo venenoso roll agregado")
#                 total+=5200
#                 producto+=1
#                 pulpo+=1
#             case 4:
#                 print("Handroll Anguila electrica roll agregado")
#                 total+=4500
#                 producto+=1
#                 ang+=1
#             case 5:
#              break
#             case _:
#                 print("Ingrese una opcion valida numerica")
#         print(f"Su cantidad d handroll son: {producto}")
#     except Exception:
#         print("Ingrese una opcion valida que no sea caracter ni decimal mamapiinga")

# while True:
#         cu=input("Ingrese su cupon o x para salir ")
#         if cu==comp:
#             desc=total*0.10
#             break
#         elif cu=="x":
#             print("No codigo")
#             break
#         else:
#             print("Ingrese una opcion valida")

                        
# print(f"""
#       =============================
#        total productos {producto}
#       ==============================
#       Pikacu roll {pik}
#       otaku roll {otak}
#       pulpo venoso roll {pulpo}
#       Anguila electrica roll {ang}
#       ==============================
#       subtotal por pagar: {total}
#       descuento por codigo: {round(desc)}
#       total: { total-desc}
#       ==============================
#       """)