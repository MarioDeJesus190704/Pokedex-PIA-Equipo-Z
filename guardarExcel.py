def guardarExcel():
    try:
        import openpyxl
    except:
        print("No se ha detectado openpyxl, favor de instalarlo")
        return()
    try:
        archivo_entrada = "datosPokemon.txt"
        archivo_salida = "pokemon_excel.xlsx"


        with open(archivo_entrada, "r") as archivo_entrada:
            datos_pokemon = []

            for linea in archivo_entrada:
                datos = linea.strip().split(",")
                datos_pokemon.append({
                    "Nombre": datos[4],
                    "Num. Pokedex": datos[3],
                    "Estatura": datos[2],
                    "Peso": datos[13],
                    "1er Tipo": datos[11],
                    "2do Tipo": datos[12],
                    "1ra Habilidad": datos[0],
                    "2da Habilidad": datos[1],
                    "Stats HP": datos[5],
                    "Stats Ataque": datos[6],
                    "Stats Defensa": datos[7],
                    "Stats Ataque Especial": datos[8],
                    "Stats Defensa Especial": datos[9],
                    "Stats Velocidad": datos[10]
                })


        libro = openpyxl.Workbook()
        hoja = libro.active

     
        encabezados = ["Nombre", "Num. Pokedex", "Estatura", "Peso", "1er Tipo", "2do Tipo",
                       "1ra Habilidad", "2da Habilidad", "Stats HP", "Stats Ataque",
                       "Stats Defensa", "Stats Ataque Especial", "Stats Defensa Especial",
                       "Stats Velocidad"]
        hoja.append(encabezados)

   
        for pokemon in datos_pokemon:
            hoja.append([
                pokemon["Nombre"], pokemon["Num. Pokedex"], pokemon["Estatura"],
                pokemon["Peso"], pokemon["1er Tipo"], pokemon["2do Tipo"],
                pokemon["1ra Habilidad"], pokemon["2da Habilidad"], pokemon["Stats HP"],
                pokemon["Stats Ataque"], pokemon["Stats Defensa"],
                pokemon["Stats Ataque Especial"], pokemon["Stats Defensa Especial"],
                pokemon["Stats Velocidad"]
            ])

       
        libro.save(archivo_salida)
        print(f"Datos guardados en {archivo_salida}")
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_entrada} no fue encontrado.")
        return()
    except Exception as e:
        print(f"Error: {e}")
        return()


if __name__ == "__main__":
    guardarExcel()

