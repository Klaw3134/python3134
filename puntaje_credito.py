# Calcular el puntaje de credito
# De bede calcular que tanto credito tiene una persona
# en cierta entidad financiera, debera considerar
# cantidad de ingresos, nivel educacional y nacionalidad
# Cantidad de ingresos
# 500.000 a 1.000.000 : 300.000
# 1.000.000 a 1.500.000: 650.000
# 1.500.001 o mas : 1.000.000
# Nivel Educacional 
# Basico : x1, medio: x1.3 , superior: x1.5
# Nacionalidad 
# Chilena : +300.000, Extranjero: +0


# ingresos=int(input("escriba su ingreso mensual"))
# educacion=input("ingrese su nivel educacional (basica-media-superior)")
# nacionalidad=input("ingrese su nacionalidad: Chilena o Extranjero")

# if ingresos>=500000 and ingresos<=1000000:
#     credito=300000
# elif ingresos>=1000000 and ingresos<=1500000:
#     credito=650000
# elif ingresos>=1500001:
#     credito=1000000
# else:
#     ingresos<500000
#     print("sujeto no valido para credito")

# if educacion.lower()=="basica":
#     nivel=1
# elif educacion.lower()=="media":
#     nivel=1.3    
# elif educacion.lower()=="superior":
#     nivel=1.5
# else:
#     print("nivel educacional no valido")

# if nacionalidad.lower()=="chilena":
#     bono=300000
# elif nacionalidad.lower()=="extranjero":
#     bono=0
# else:
#     print("nacionalidad no valida")

# ptecredi=(credito*nivel)+bono
# print(f"credito final: ${ptecredi}")

# ############Simula el movimiento de un jugador en un tablero
# lineal de 30 casillas. El jugador lanza un dado virtual 
# (genera un número aleatorio entre 1 y 6) en cada turno y 
# avanza esa cantidad de casillas. El objetivo es llegar o superar
# la casilla 30.


############### import random
# import time

# jugador=0
# meta=30

# print(F"posicion del jugador: {jugador}")
      
# while jugador<meta:


# Clasificar segun categoria y precio
# Cat 1 +200, cat 2 +400, cat 3 +600
# Decuento Precios : 1000 y menos;3%, entre 1001 y 5000 
# ;5% , 5001 y mas 6%
# Poner listado de 3 productos por categoria, las cat son 1 ,2 y 3
# Agregar los impuestos al ´precio , segun la cat y luego 
# aplicar descuento al total de la boleta segun el monto

# Ej:
# Producto 1, cat 2, 1500 + 400
# Producto 2 cat 1, 8000 + 200
# EL total es 10100 * - 6%
# EL total a pagar es: 9494

# categorias=int(input('''
#                      Categoria: 1.- productos de aseo (cloro-quix-esponja)
#                                  2.- verduras (tomate-lechuga-apio)
#                      3.- abarrotes (arroz-fideos-atun)'''))

# if categorias==1:
#     add=+200
# elif categorias==2:
#     add=+400
# elif categorias==3:
#     add=+600
# else:
#     print("elija opcion valida")


# productos=


total = 0
contador = 1

while contador <= 3:
    print("Producto", contador)
    
    precio = int(input("Ingresa el precio del producto: "))
    categoria = int(input("Ingresa la categoría (1, 2 o 3): "))
    
    # Sumar impuesto según categoría
    if categoria == 1:
        impuesto = 200
    elif categoria == 2:
        impuesto = 400
    elif categoria == 3:
        impuesto = 600
    else:
        impuesto = 0  # Por si ingresan una categoría incorrecta

    precio_con_impuesto = precio + impuesto
    total = total + precio_con_impuesto

    contador = contador + 1

# Aplicar descuento según total
if total <= 1000:
    descuento = total * 0.03
elif total <= 5000:
    descuento = total * 0.05
else:
    descuento = total * 0.06

total_final = total - descuento

# Mostrar resultados
print("El total antes del descuento es:", total)
print("Descuento aplicado:", descuento)
print("El total a pagar es:", total_final)total = 0
contador = 1