def datos_poke():
    try:    #Verificamos que se pueda abrir el archivo de texto
        fo = open("datosPokemon.txt", "r")
    except: #En caso de que no se pueda abrir, marcar error y mandar al menu principal
        print("Error al abrir el archivo, intente hacer una busqueda en la API para generarlo.")
        return()

    encontrado = False
    busqueda = input("Ingrese nombre o numero de pokedex del pokemon a buscar: ")
    
    for line in fo:
        datos = line.split(",")
        if busqueda.lower() == datos[4] or busqueda.lower() == datos[3]:
            encontrado = True
            print("Nombre:",datos[4])
            print("Num. Pokedex:",datos[3])
            print("Estatura:",datos[2])
            print("Peso:",datos[13])
            print("1er Tipo:",datos[11])
            print("2do Tipo:",datos[12])
            print("1ra Habilidad:",datos[0])
            print("2da Habilidad:",datos[1])
            print("Stats:\tHP:",datos[5])
            print("\tAtaque:",datos[6])
            print("\tDefensa:",datos[7])
            print("\tAtaque Especial:",datos[8])
            print("\tDefensa Especial:",datos[9])
            print("\tVelocidad:",datos[10])
    if encontrado == False:
        print("Pokemon desconocido.")
        return()
    fo.close()

if __name__ == "__main__":
    datos_poke()
