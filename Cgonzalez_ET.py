#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video],
...
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
           'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}


#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
         'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}




def stock_marca(Productos,stock):
    marca=input("Ingrese marca a consultar")
    for i,n in productos.items():
        print(f'''marca:{n[0]}
                  modelo:{stock[i][0]}
                  modelo:{stock[i][1]}
                modelo:{stock[i][2]}
              
              
              ''')
        
def mostrar(productos,stock):
    print("Listado de productos")
    for i,n in productos.items():
        print(i,n)

def actprec(productos,stock):
    mostrar(productos,stock)
    act=input("Ingrese modelo a actualizar")
    if act in stock:
        nuevo=int(input("Ingrese nuevo precio"))
        stock[act][0][1][2]=act
        print("Precio actualizado")
    else:
        print("Ingrese un modelo valido")   

def busqueda(productos,stock):
    b=int(input("ingrese precio minimo"))
    b2=int(input("ingrese precio maximo"))
    if b>=200000 and b2<=750000:
     print("Los notebooks entre los precios que consultas son: ")
     mostrar(productos,stock)
    else:
        print("No tenemos notebooks en ese rango de precios")



     
while True:
    try:
        op=int(input(''' Menú Principal
                           1. Stock marca.
                           2. Búsqueda por precio.
                           3. Actualizar precio.
                           4. Salir


                             '''))
        match op:
            case 1:
                stock_marca(productos,stock) 
            case 2:
                busqueda(productos,stock)
            case 3:
                actprec(productos,stock)
            case 4:
                print("saliendo...")
                break 
            case _:
                print("ingrese una opción valida")       
    except Exception as e:
        print(e)    
