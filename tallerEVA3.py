## ejemplo de carrito con categorias
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

import random
while True:
    try:
        cantniños=int(input("Cuantos niños van a buscar Huevos?"))
        while cantniños<0:
            print("ERROR, solo ingrese numero positivos")
            cantniños=int(input("Cuantos niños van a buscar huevos?"))

        noob=0
        master=0
        legend=0
        top=0
        for n in range(cantniños):
            canthuevos=random.randint(5,30)
            if canthuevos>top:
                top=canthuevos

            print(f"el niño numero{n+1} encontró {canthuevos}, huevos")
            if canthuevos<12:
                noob+=1
            elif canthuevos>=12 and canthuevos<=24:
                master+=1
            else:
                legend+=1
        print("la cantidad del grupo noob es", noob)                    
        print("la cantidad del grupo master es", master)                    
        print("la cantidad del grupo legend es", legend)                    
        print("la mayor cantidad de huevos encontrada por un niño fue:" , top)
        break
    except Exception:
        print("solo numeros enteros")                    

        



                        
