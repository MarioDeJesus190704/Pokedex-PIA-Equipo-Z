def graf_promedio_tipo():
    try:    #Verificamos que se pueda abrir el archivo de texto
        fo = open("datosPokemon.txt", "r")
    except: #En caso de que no se pueda abrir, marcar error y mandar al menu principal
        print("Error al abrir el archivo, intente hacer una busqueda en la API para generarlo.")

    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except:
        print("No se han detectado matplotlib, favor de instalarlo")
        return()
    
    stats = {
        "HP" : 0,
        "Ataque" : 0,
        "Defensa" : 0,
        "Ataque Especial" : 0,
        "Defensa Especial" : 0,
        "Velocidad" : 0}

    encontrado = False
    conta = 0
    busqueda = input("Ingresa el tipo a promediar: ")
    
    for line in fo:
        datos = line.split(",")
        if busqueda.lower() == datos[11] or busqueda.lower() == datos[12]:
            encontrado = True
            stats["HP"] += int(datos[5])
            stats["Ataque"] += int(datos[6])
            stats["Defensa"] += int(datos[7])
            stats["Ataque Especial"] += int(datos[8])
            stats["Defensa Especial"] += int(datos[9])
            stats["Velocidad"] += int(datos[10])
            conta += 1
    if encontrado == False:
        print("Tipo desconocido.")
        return()
    fo.close()
    prom = list()
    print("Promedio de stats en el tipo "+busqueda,"con total de",conta,"pokemon:")
    for x,y in stats.items():
        promedio = y/conta
        #print(x,":",prome)
        prom.append(promedio)
    
    x = ("Velocidad", "Defensa Esp.", "Ataque Esp.", "Defensa", "Ataque", "HP")
    y = np.array([prom[5],prom[4],prom[3],prom[2],prom[1],prom[0]])
    titulo = "Promedio de stats del tipo: " + busqueda
    colores = ['#b19cd9', '#bae1ff', '#baffc9', '#ffffba', '#ffdfba', '#ffb3ba']
    plt.barh(x, y, color = colores)
    plt.title(titulo)
    plt.ylabel("Tipos de stats")
    plt.xlabel("Promedio de stats")
    plt.axis(xmin = 0, xmax = 170)
    plt.show()


if __name__ == "__main__":
    graf_promedio_tipo()
