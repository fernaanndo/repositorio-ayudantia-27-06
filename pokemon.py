pokemones = {
    'PIK025': ['Ash',   'Pikachu',   'Eléctrico', 'Kanto', 1, 'Alegre',    'Impactrueno'],
    'CHA006': ['Ash',   'Charizard', 'Fuego',     'Kanto', 1, 'Audaz',     'Lanzallamas'],
    'STA121': ['Misty', 'Starmie',   'Agua',      'Kanto', 1, 'Serena',    'Hidrobomba'],
    'ONI095': ['Brock', 'Onix',      'Roca',      'Kanto', 1, 'Firme',     'Lanzarrocas'],
    'EEV133': ['Gary',  'Eevee',     'Normal',    'Kanto', 1, 'Tímida',    'Placaje'],
    'BLA257': ['May',   'Blaziken',  'Fuego',     'Hoenn', 3, 'Osada',     'Patada ígnea'],
    'GAR282': ['May',   'Gardevoir', 'Psíquico',  'Hoenn', 3, 'Modesta',   'Psíquico'],
    'UMB197': ['Gary',  'Umbreon',   'Siniestro', 'Johto', 2, 'Cautelosa', 'Bola sombra'],
}


registro = {
    'PIK025': [1320, 3],
    'CHA006': [2890, 1],
    'STA121': [1450, 2],
    'ONI095': [980, 4],
    'EEV133': [640, 5],
    'BLA257': [2540, 1],
    'GAR282': [2310, 2],
    'UMB197': [1780, 1],
    'MAG129': [310, 0],
}


def menu():
    print("*** MENU PRINCIPAL ***")
    print("1.- Pokemon por entrenador")
    print("2.- Busqueda por poder de combate")
    print("3.- Actualizar poder de combate")
    print("4.- Salir")


def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion del menu: "))
            return opcion
        except ValueError:
            print("Debe ingresar valores enteros")


def existe_entrenador(entrenador):
    for valor in pokemones.values():
        if valor[0].strip().lower() == entrenador.strip().lower():
            return True
    return False


def pokemon_entrenador(entrenador):
    if existe_entrenador(entrenador) == True:
        cantidad = 0
        for clave, valor in pokemones.items():
            if valor[0].strip().lower() == entrenador.strip().lower():
                cantidad+=registro[clave][1]
        print(f"La cantidad de pokemones del entrenador {entrenador} es: {cantidad}")
    else:
        print("No existe ese entrenador")



def busqueda_poder(p_min, p_max):
    lista=[]
    for clave, valor in registro.items():
        if valor[0] >= p_min and valor[0] <= p_max and valor[1] != 0:
            entrenador = pokemones[clave][0]
            lista.append(entrenador + "--" + clave)
    lista.sort()
    print(lista)




def ejecutar_software():
    while True:
        menu()
        opcion = ingresar_opcion()
        
        if opcion == 1:
            entrenador = input("Ingrese el nombre del entrenador: ").strip().lower()
            pokemon_entrenador(entrenador)
        elif opcion == 2:
            while True:
                try:
                    p_min= int(input("Ingrese el poder minimo: "))
                    p_max= int(input("Ingrese el poder maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!")
            
            busqueda_poder(p_min, p_max)
        




ejecutar_software()