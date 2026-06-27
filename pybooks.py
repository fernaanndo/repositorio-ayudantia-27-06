productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'], 
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'], 
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'], 
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'], 
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'], 
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'], 
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'], 
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
} 
# Este es un comentario
stock = {
    '8475HD': [387990,10],
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1], 
    'fgdxFHD': [664990,21],
    '123FHD': [290890,32],
    '342FHD': [444990,7], 
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1],
    'FS1230HD': [249990,0],
}  


def menu():
    print("*** MENU PRINCIPAL ***")
    print("1.- Stock marca")
    print("2.- Busqueda por precio")
    print("3.- Actualizar precio")
    print("4.- Salir")


def elegir_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion del menu: "))
            return opcion
        except ValueError:
            print("Debe ingresar un numero entero como opcion")


def stock_marca(marca):
    suma_stock = 0
    for producto in productos:
        if productos[producto][0].strip().lower() == marca:
            suma_stock+=stock[producto][1]
    
    return suma_stock


def busqueda_precio(p_min, p_max): 
    # Deebemos guardar en el siguiente formato -> Marca--Modelo
    modelos = []
    for clave, valor in stock.items():
        if valor[0] >= p_min and valor[0] <= p_max and valor[1] != 0:
            marca = productos[clave][0]
            modelos.append(marca + "--" + clave)
    modelos.sort()
    return modelos
        


def existe_modelo(modelo):
    if modelo in stock:
        return True
    else:
        return False

        
def actualizar_precio(modelo, p):
    if existe_modelo(modelo):
        stock[modelo][0] = p
        return True
    else:
        return False





def ejecutar_software():
    while True:
        menu()
        opcion = elegir_opcion()
        if opcion == 1:
            marca = input("Ingrese la marca de la que desea saber el stock: ").strip().lower()
            stock = stock_marca(marca)
            print(f"El stock es: {stock}")
        elif opcion == 2:
            while True:
                try:
                    precio_minimo = int(input("Ingrese precio minimo: "))
                    precio_maximo = int(input("Ingrese precio maximo: "))
                    break   
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            modelos = busqueda_precio(precio_minimo, precio_maximo)
            if len(modelos) == 0:
                print("No hay notebooks en ese rango de precio")
            else:
                print(modelos)
        elif opcion == 3:
            while True: 
                modelo_actualizar = input("Ingrese el modelo que desea actualizar: ")
                while True:
                    try:
                        precio_nuevo = int(input("Ingrese le precio nuevo: "))
                        break
                    except ValueError:
                        print("Debe ingresar un precio valido")
                
                if actualizar_precio(modelo_actualizar, precio_nuevo) == True:
                    print("Actualizado!")
                else:
                    print("Ese modelo no existe")
                
                respuesta = input("Desea actualizar otro precio?: ").strip().lower()
                if respuesta != "si":
                    break
        elif opcion == 4:
            print("Programa finalizado")
            break
        else:
            print("Debe ingresar una opcion valida")




ejecutar_software()


