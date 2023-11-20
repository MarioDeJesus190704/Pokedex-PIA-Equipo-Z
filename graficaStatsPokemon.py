def graf_stats():
    try:    #Verificamos que se pueda abrir el archivo de texto
        fo = open("datosPokemon.txt", "r")
    except: #En caso de que no se pueda abrir, marcar error y mandar al menu principal
        print("Error al abrir el archivo, intente hacer una busqueda en la API para generarlo.")
        return()

    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except:
        print("No se han detectado matplotlib, favor de instalarlo")
        return()

    encontrado = False
    busqueda = input("Ingrese nombre o numero de pokedex del pokemon a graficar: ")
    
    for line in fo:
        datos = line.split(",")
        if busqueda.lower() == datos[4] or busqueda.lower() == datos[3]:
            encontrado = True
            x = ("Velocidad", "Defensa Esp.", "Ataque Esp.", "Defensa", "Ataque", "HP")
            y = np.array([int(datos[10]),int(datos[9]),int(datos[8]),int(datos[7]),int(datos[6]),int(datos[5])])
            titulo = "Stats de " + datos[4]
            colores = ['#b19cd9', '#bae1ff', '#baffc9', '#ffffba', '#ffdfba', '#ffb3ba']
            plt.barh(x,y, color = colores)
            plt.title(titulo)
            plt.ylabel("Tipos de stats")
            plt.xlabel("Numero de stats")
            plt.axis(xmin = 0, xmax = 170)
            plt.show()
            
    if encontrado == False:
        print("Pokemon desconocido.")
        return()
    fo.close()

if __name__ == "__main__":
    graf_stats()
