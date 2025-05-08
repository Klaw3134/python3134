
import random
# numAzar=random.randint(1,10)
# print(numAzar)

#necesito al menos 20 puntos para abrir la puerta
# if numAzar>=20:
#     print("puede pasar")
# else:
#     print("le falta puntaje")


## generar un num aleatoreo entre 1 y 50
# pedir al usuario un nummero
# si ingresa un numero mayor decirle, "el num a adivinar es menor"
# si ingresa un numero menor decirle, "el numero a adivinar es mayor"
# ej: numeroAdivinar=20


# numAdivinar=random.randint(1,50)
# num=int(input("adivine el numero"))
# while num!=numAdivinar:
#     # print(numAdivinar)
#     if num>numAdivinar:
#         print("elnumero a adivinar es menor")
#     else:
#         print("el numero a adivinar es mayor")
#     num=int(input("adivine el numero"))
# print("le achuntaste!")            

# ruleta rusa
# barril=random.randint(1,6)
# rul=int(input("adivine el numero"))
# while rul!=barril:
#     rul=int(input("dispare"))
# print("BANG!!")    


# LUDO
import time


# j1=0
# j2=0
# meta=30
# turno=1

# while j1<meta and j2<meta:
#         if turno % 2 == 0:
#             print("Turno de J1")
#             time.sleep(1)
#             dado=random.randint(1, 6)
#             j1+=dado
#             print(f"EL J1 sacó {dado}")
#             print(f"Avanza hasta la casilla {j1}")
#         else:
#             print("Turno de J2")
#             time.sleep(1)
#             dado=random.randint(1, 6)
#             j2+=dado
#             print(f"EL J2 sacó {dado}")
#             print(f"Avanza hasta la casilla {j2}")
#         turno += 1

# if j1 > j2:
#         print("El ganador es J1")
# else:
#         print("El ganador es J2")



 # La florida 20%, la pintana 30%, Puente alto 25%, Sn joaquin 15%
 # grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
 # preguntar al usuario en que comuna vive
 # preguntar al usuario con cuantas personas vive
 # el arancel actual es de 200.000 por semestre
 # basados en la respuestas del usuario y en 
 # la informacion dada, calcular su descuento

 #ingrese su comuna: la florida
 #ingrese su grupo familiar (numeero entero ud incluido): 4
 # total de dscto es de 23%
 #total a pagar es de $154.000


# arancel=200000
# descuento=0
# print('''
#      1.- la floridam 20%
#      2.- la pintana 30%
#      3.- puente asalto 25%
#      4.- sanjoaco 15%  
#       ''')

# comuna=int(input("ingrese su comuna"))

# if comuna==1:
#     descuento=20
# elif comuna==2:
#      descuento=30
# elif comuna==3:
#      descuento=25
# elif comuna==4:
#      descuento=15
# else:
#      print("Seleccion incorrecta")

# grupo=int(input("ingrese grupo familiar ( num entero ud incluido)"))

# if grupo==1:
#     descuento+=2
# elif grupo<=4 and grupo>=2:
#      descuento+=3
# elif grupo>=5:
#      descuento+=4

# else:
#      print("Seleccion incorrecta")

# print("el descuento total es", descuento)
# desc=arancel*descuento/100
# total=arancel-desc
# print("el total a pagar es $", total)

#  Gerenear un numero aleatoreo entre 1 y 50
# Pedir al usuario un numero
# Si ingresa un numero mayor  decirle, 
# " El numero a adivinar es menor".
# Si ingresa un numero menor  decirle,
#  " El numero a adivinar es mayor".
#EJ numeroAadivinar= 20 
# Si ingresa el 15 debe decir, " El numero a adivinar es mayor" .
# Si ingresa el 35 debe decir, " El numero a adivinar es menor" .
 

import random

numAdivinar=random.randint(1,50)
num=int(input("adivine el numero"))
while num!=numAdivinar:
    # print(numAdivinar)
    if num>numAdivinar:
        print("elnumero a adivinar es menor")
    else:
        print("el numero a adivinar es mayor")
    num=int(input("adivine el numero"))
print("le achuntaste!")           

