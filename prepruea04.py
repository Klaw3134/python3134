juegos={
    1:{"nombre": "metroid dread",
    "precio": 55000,
    "code": "jaksjdk87"
      },
    2:{"nombre": "metroid dread",
    "precio": 55000,
    "code": "jaksjdk87"
      },
}

def mostrar_juegos(dict):
    for key,juego in dict.items():
        print(key ,juego)
def valida_codigo(code):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for codigo in code:
        if codigo.isupper():
            Mayuscula+=1
        if codigo.islower():
            Minuscula+=1
        if codigo.isdigit():
            Numero+=1
    if Mayuscula==2 and Minuscula==2 and Numero==4:
        print("El codigo está bien escrito")
        return True
    else:
        print("la codigo está mal escrito")
        return False

def insertar_juego(dict):
    nombre=input("Ingrese un nombre: ")
    precio=int(input("Ingrese la raza: "))
    codigo=input("Ingrese su codigo: ")
    valida_codigo(codigo)
    pos=list(dict.keys())[-1]
    dict[pos+1]={"nombre":nombre, "precio":precio, "code":codigo} 

def valida_precio(p):
    if p>=8000 and p<=100000:
        return True
    else:
        return False

def valida_nombre(N):
    for l in N:
        if " " ==1:
            return True        

    

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
                
            case 2:
                mostrar_juegos(perros)
            case 3:
        
            case 4 :
                
            case 5:
                break
            case _:
                    print("Opcion invalida")
     except Exception as e:
        print("EL error es: ", e)    

