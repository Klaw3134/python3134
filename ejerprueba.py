### perros de caza
### pida al usuario la cantidad de perros
### muestre cual es la cuota minima de conejos
### luego consulte cuantos conejos trajo
### sie el perro trajo la cantidad minima
### cumplio la cuota, sino, se queda sin filete
### mostrar resumen de perro que cumplieron y los que no


# import random, time

# while True:
#     try:
#         perro=int(input(" Ingrese un numero: "))
#         break
#     except Exception:
#         print("solo se permiten numeros enteros")
# cuota=5
# psi=0
# pno=0
# conejot=0
# print("la cuota minima por perro es de 5 conejos")

# for i in range(perro):
#     time.sleep(1)
#     rabb=random.randint(0,20)
#     conejot+=rabb
#     print(f"el perro {i+1} trajo {rabb} conejos")
#     if rabb>=cuota:
#         print("tiene filete")
#         psi+=1
#     else:
#         print("El perro no cumplió con la cuota")
#         pno+=1         #### variable (perros-psi)

# print("-------resumen------")
# print(f"perros que cumplieron la cuota {psi} c:")
# print(f"Perros que no cumplieron {pno} :(")
# print(f"La cantidad total de conejos fue {conejot}")



### Quiere pasar el ramo?
# pregunte la cantidad de rojos en el curso
#los talleres que hay en el semestre son 4
#por cada taller asistido obtiene 0.3 decimas
#si el alumno tiene mas de 1 punto 
# tiene la bendicion del profe
# sino, no se le puede ayudar
#ingrese la nota final y sume las decimas acumuladas
# muestre si aprueba o reprueba


# import random

# tallerT=4
# dec=0
# rojo=int(input("Ingrese la cantidad de alumnos con nota roja:"))
# for al in range (rojo):
#     for t in range (tallerT):
       
#         print(f"el alumno asistio al taller {t+1}")
#         resp=random.randint(1,2)
#         if resp==1:
#             dec+=0.3
#     if dec>=1:
#         print("tiene la bendi del profe")
#     else:
#      print("si no se ayuda, el profe tampoco puede")
#     NT=float(input("cual es su nota final"))
#     print("sus decima totales fueron" , dec)
#     NT+=dec                  
#     if NT>=4:
#             print("El alumno aprobo")
#     else:
#             print("El alumno reprobó")



# while True:
#     print('''
#           Seleccione una opcion:
#           1.- Teclados
#           2.- Monitores
#           3.- Audifonos
#           4.- Pagar
#           5.- Salir''')
#     op=int(input())
#     match op:
#         case 1:
#             print('''
#           Seleccione una opcion:
#           1.- Teclados gamer $8000
#           2.- Teclado aburrido $8.0000
#           3.- volver al menu principal''')
#     op=int(input())    
#             case 2:

#             case 3:
#             case 4:






####### EJERCICIO 2.5.3

# deuda=100000

# while True:
#     ('''
#     Selencione una opcion:
#     1.- Pago de Tarjeta
#     2.- Simulación de compra
#     3.- saldo actual de la tarjeta
#     4.- Salir
    
#     ''')
#     op=int(input())
#     match op:
#             case 1:
#                 while True:
#                  try:
#                   deuda=100000
#                   print(f"su deuda actua es de $ {deuda}")
#                   pago=int(input("Cuanto desea abonar?"))
#                   if pago<=0:
#                       print("El monto debe ser mayor a cero")
#                   elif pago==deuda:    
#                       print("Pago realizado")
#                    else
                  
              


### EVALUACION FORMATIVA 3
######

while True:
    try:
        (''' Seleccione las opciones a llevar:
        1.-PIKACHU ROLL $4500
        2.-OTAKU ROLL $5000
        3.-PULPO VENENOSO ROLL $5200
        4.-ANGUILA ELECTRICA ROLL $4800
        5.- Salir
        ''')
        op=int(input())
        match op:
            case 1:
            case 2:
            case 3:
            case 4:        

    
    except Exception:
                         
                

