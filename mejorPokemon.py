def mejorPokemonPorTipo():
    try:
        import openpyxl
    except ImportError:
        print("No se ha detectado openpyxl, favor de instalarlo")
        return()

    try:
        archivo_entrada = "pokemon_excel.xlsx"
        workbook = openpyxl.load_workbook(archivo_entrada)
        sheet = workbook.active

        mejores_pokemon_hp = {}

        encabezados = [cell.value for cell in sheet[1]]

        tipo_column_index = encabezados.index("1er Tipo")
        nombre_column_index = encabezados.index("Nombre")
        hp_column_index = encabezados.index("Stats HP")

        for row in sheet.iter_rows(min_row=2):
            tipo = row[tipo_column_index].value
            nombre = row[nombre_column_index].value
            hp = row[hp_column_index].value

            if tipo != "N/A":
                if tipo not in mejores_pokemon_hp or hp > mejores_pokemon_hp[tipo][1]:
                    mejores_pokemon_hp[tipo] = (nombre, hp)

        print("Pokémon con mayor Stats HP por tipo:")
        for tipo, (nombre, hp) in mejores_pokemon_hp.items():
            print(f"{tipo}: {nombre} (Stats HP: {hp})")

    except FileNotFoundError:
        print(f"Error antes de ocupar esta opcion primero es necesario crear el Exel.")
        return()
    except Exception as e:
        print(f"Error: {e}")
        return()

if __name__ == "__main__":
    mejor_pokemon_por_tipo()
