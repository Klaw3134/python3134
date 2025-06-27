
def mostrar_juegos(dict):
    for key,juego in dict.items():
        print(key ,juego)
def valida_code(clave):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for palabra in clave:
        if palabra.isupper():
            Mayuscula+=1
        if palabra.islower():
            Minuscula+=1
        if palabra.isdigit():
            Numero+=1
    if Mayuscula==2 and Minuscula==2 and Numero==4:
        print("El codigo está bien escrito")
        return True
    else:
        print('''El codigo del juego debe tener 2 mayusculas, 2 minisculas
                    y 4 numeros ''')
        return False
def valida_precio(p):
    if p>=8000 and p<=100000:
        return True
    else:
        return False
def valida_nombre(N):
    for l in N:
        if " " ==l:
            return True   
def insertar_juego(dict):
    while True:
        nombre=input("Ingrese un nombre: ")
        if valida_nombre(nombre):
            break
        else:
            print("el nombre del juego debe tener almenos 2 palabras")
    while True:        
        precio=int(input("Ingrese el precio: "))
        if valida_precio(precio):
            break
        else:
            print("El precio debe estar entre $8000 y $100000")
    while True:        
        codigo=input("Ingrese su codigo: ")
        if valida_code(codigo):
            pos=list(dict.keys())[-1]
            dict[pos+1]={"nombre":nombre, "precio":precio, "code":codigo} 
            break
        else:
            print("No se agregó el juego")
def actualizar_juegos(dict):
    mostrar_juegos(dict)
    act=int(input("Seleccione el juego a actualizar: "))
    while True:
        print('''  1.-nombre
                   2.-precio
                   3.-codigo
                   4.-salir   
                  ''')
        dato=int(input("qué dato va a actualizar?:" ))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre: ")
                if valida_nombre(n):
                    dict[act]["nombre"]=n
                else:
                    print("elnombre del juego debe tener al menos dos palabras")
            case 2:
                n=int(input("ingrese el nuevo precio"))
                if valida_precio(n):
                    dict[act]["precio"]=n
                else:
                    print("el precio debe estar entre $8000 y $100000")
            case 3:
                n=input("ingrese el  nuevo codigo")
                if valida_code(n):
                    dict[act]["codigo"]=n
                else:
                     print("el paramatro del codigo no es correcto")
                     print('''
                    el codigo debe tener, una mayuscula, una minuscula, 
                    un numero y un largo exacto de 6''')        
            case 4:
                break
            case _:
                print("Opción invalida")                                                
def borrar_juegos(dict):
#     mostrar_juegos(dict)
#     borrar=int(input("Que juego deseas borrar"))
#     del juegos[borrar]





juegos={
    1:{"nombre":"Metroid Dread",
       "precio": 55000,
       "code": "MtDr2022"
       },
    2:{"nombre":"Zelda TOTK",
       "precio": 65000,
       "code": "zdTK2025"
       }
}

while True:
     try:
        print('''
              1.- Registrar un juego
              2.- Mostrar juegos
              3.- Actualizar juego
              4.- Borrar juego
              5.- Salir
              ''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                insertar_juego(juegos)   
            case 2:
                mostrar_juegos(juegos)
            case 3:
                actualizar_juegos(juegos)
            case 4 :
                borrar_juegos(juegos)
            case 5:
                break
            case _:
                    print("Opcion invalida")
     except Exception as e:
        print("EL error es: ", e)    





Parkins={
    1:{"marca":"Toyota",
       "año":1998,
       "patente":"abc123",
       "tipo":"auto"},
    2:{"marca":"Hiundai",
       "año":1995,
       "patente":"abc456",
       "tipo":"auto"}
}
def agregar(parkin):
    while True:
        try:
                marcau=input("Ingrese nombre: ")
                añou=int(input("Ingrese año: "))
                validarA(añou)
                patenteu=input("Ingrese patente: ")
                validarP(patenteu)
                tipou=input("Ingrese tipo: ")
                llave=list(parkin.keys())[-1]
                parkin[llave+1]={"marca":marcau,"año":añou,"patente":patenteu,"tipo":tipou}
                break   
        except Exception as e:
            print(e)

def validarP(variable):
    while True:
        try:
            minu=0
            numeros=0
            for letra in variable:
                if letra.islower():
                    minu+=1
                if letra.isdigit():
                    numeros+=1
            if minu==4 and numeros==2:
                print("La patente esta bien escrita")
                return True
            else:
                print("La patente esta mal escrita, debe tener 4 letras y 2 digitos")
                variable=input("Ingrese patente: ")
        except Exception as e:
            print(e)
        
            
def validarA(año):
   cont=0
   for digito in str(año):
     cont+=1
   if cont==4:
     return True
   elif cont>4 or cont<4:
     print("Debe tener 4 digitos")
     año=int(input("Ingrese año: "))
        
        
    
        
def mostrar(parkins):
     for llave,valor in parkins.items():
         print("ID ",llave,valor)

def actualizar(parkins):
    mostrar(parkins)
    while True:
        iden=int(input("Ingrese ID que desea actualizar: "))
        if iden in parkins:
            añov=False
            patentev=False
            while True:
                try:
                        marcau=input("Ingrese nombre: ")
                        añou=int(input("Ingrese año: "))
                        añov=validarA(añou)
                        patenteu=input("Ingrese patente: ")
                        patentev=validarP(patenteu)
                        tipou=input("Ingrese tipo: ")
                        parkins[iden]={"marca":marcau,"año":añou,"patente":patenteu}
                        break   
                except Exception as e:
                    print(e)
        else:
            print("Ingrese un id valido")
        break
 
def estadistica(parkin):
    total=0
    for llave in parkin:
         total+=1
    print(f"Autos guardados: {total}")
    iden=list(parkin.keys())[-1]
    ultimo=parkin[iden]
    print(f"El ultimo ingreso fue: {ultimo}")
    
         
         
                        
while True:
    try:
        op=int(input(""""
                      1.- Ingresar Vehiculo
                      2.- Mostrar Vehiculos
                      3.- Actualizar Vehiculo
                      4.- Marcar salida de Vehiculo con hora*
                      5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
                      6.- Salir"""))
        match op:
            case 1:
                agregar(Parkins)
            case 2:
                mostrar(Parkins)
            case 3:
                actualizar(Parkins)
            case 4:
                print()
            case 5:
                estadistica(Parkins)
            case 6:
                exit()
                
    except Exception as e:
        print(e)