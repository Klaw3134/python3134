
# for i in range(1,6):
#     print(i)

# num=9

# for i in range(1,11):
#     print(num, "x" , i , "=" , i*num)

# num=9

# for j in range(1,11):
#         print (f"la tabla del {j}")
#         for i in range (1,11)
#         print(j, "x" , i , "=" , i*j)

## preguntar la cantidad de notas y promediarlas


# cantN=int(input("ingresa cantidad de notas"))
# suma=0
# for i in range(cantN):
#     print(f"ingrese la nota numero{i+1}")
#     nota=float(input())
#     suma=suma+nota
# prom=suma/cantN
# print(f"el promedio es {prom}")

# if prom>=4.0:
#     print(input("aprobado"))
# else: prom<4.0
# print(input("reprobado"))

## preguntar al usuaroo cuantos productos llevará
## escribir listado de 3 productos y sus precios
#mostrar el total neto de la compra
#mostrar total del iva

# cant=int(input("ingresa cantidad de productos"))
# total=0
# for i in range(cant):
#     print( '''
#         "Que producto llevará?"
# 		 "1.- Diazepam $9000"
# 		 "2.- Metametozona $18500"
# 		 "3.- Oblea China $1000"
          
#           ''')
#     op=int(input())
#     if op==1:
#         print("usted lleva diazepam")
#         total=total+9000
#     elif op==2:
#         print("usted lleva Metametazona")
#         total=total+18500
#     elif op==3:
#         print("usted lleva Oblea China")
#         total=total+1000
#     else:
#         print("error, seleccione opcion valida") 

# print("el total neto es", total)
# print("el total con IVA es", total*1.19)    


#VOTATOON
# DESIGNE DOS CANDIDATOS PREGUNTE CUANTOS VOTTANTES SON, por cada votante debe preguntar por quien votará
# cuente cantidad de votas y muestre los resultados
# definir quien ganó la votacion
# Considere empate

c1="shaggy"
c2="Dexter"
cv1=0
cv2=0
cant=int(input("ingresa cantidad de votantes"))
for i  in range (cant):
    print(f"Seleccione a su candidato: 1.- {c1} , 2.-{c2}")
    voto=int(input)
    if voto==1:
        cv1+=1
    else:
        cv2+=1
print(f"la cantidad de votos de {c1} es {cv1}")     
print(f"la cantidad de votos de {c2} es {cv2}")     
if cv1>cv2:
    print(f"el ganador es {c1}") 
elif  cv1<cv2:
    print(f"el ganador es {c2}")  
else:    