def pokemon_tipo():
    try:    #Verificamos que se pueda abrir el archivo de texto
        fo = open("datosPokemon.txt", "r")
    except: #En caso de que no se pueda abrir, marcar error y mandar al menu principal
        print("Error al abrir el archivo, intente hacer una busqueda en la API para generarlo.")
    stats = {
        "HP" : 0,
        "Ataque" : 0,
        "Defensa" : 0,
        "Ataque Especial" : 0,
        "Defensa Especial" : 0,
        "Velocidad" : 0}

    encontrado = False
    conta = 0
    busqueda = input("Ingresa el tipo a buscar: ")
    
    for line in fo:
        datos = line.split(",")
        if busqueda.lower() == datos[11] or busqueda.lower() == datos[12]:
            encontrado = True
            conta += 1
    if encontrado == False:
        print("Tipo desconocido.")
        return()
    fo.close()

    print("El tipo",busqueda,"tiene:",conta,"pokemon")


if __name__ == "__main__":
    pokemon_tipo()
