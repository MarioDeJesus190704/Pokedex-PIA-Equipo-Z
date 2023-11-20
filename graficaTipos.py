def graf_tipos():
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
    tipos = {
        "normal" : 0,
        "fire" : 0,
        "fighting" : 0,
        "water" : 0,
        "flying" : 0,
        "grass" : 0,
        "poison" : 0,
        "electric" : 0,
        "ground" : 0,
        "psychic" : 0,
        "rock" : 0,
        "ice" : 0,
        "bug" : 0,
        "dragon" : 0,
        "ghost" : 0,
        "dark" : 0,
        "steel" : 0,
        "fairy" : 0}
    
    for line in fo:
        for x in tipos.keys():
            datos = line.split(",")
            if x == datos[11] or x == datos[12]:
                tipos[x] += 1
    fo.close()
    #print(tipos)
    x = ('normal', 'fire', 'fighting', 'water', 'flying', 'grass', 'poison', 'electric',
         'ground','psychic', 'rock', 'ice', 'bug', 'dragon', 'ghost', 'dark', 'steel', 'fairy')
    y = list()
    colores = ["#9e9e9e", "#ff5e00", "#a30000", "#0080ff", "#8fa6b5", "#00ba32", "#a82eff", "#fff700",
               "#9e5d28", "#ffb3f2", "#2b2b2b", "#99fffc", "#c5ffbf", "#ff4dbe", "#7d54b3", "#000000", "#5c5c5c", "#fbbdff"]
    for val in tipos.values():
        y.append(val)
    plt.barh(x,y, color = colores)
    plt.title("Grafica de cuantos pokemon hay por tipo")
    plt.xticks(range(0, 36, 2))
    plt.ylabel("Tipos")
    plt.xlabel("Num. de pokemon")
    plt.show()
    
if __name__ == "__main__":
    graf_tipos()
