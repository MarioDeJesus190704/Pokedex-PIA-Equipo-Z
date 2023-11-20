try:
    from API_Call import api_call
    from datosPokemon import datos_poke
    from graficaStatsPokemon import graf_stats
    from promedioTipo import promedio_tipo
    from graficaPromedioTipo import graf_promedio_tipo
    from guardarExcel import guardarExcel
    from mejorPokemon import mejorPokemonPorTipo
    from graficaTipos import graf_tipos
    from pokemonTipo import pokemon_tipo
except:
    print("Error: No se detecta los programas .py para los modulos.")
    input("Cerrando programa...")
    exit()

def valid_menu(menu):
    print(menu)
    try:
        op = int(input("?"))
    except ValueError:
        print("Error de valor: Favor de ingresar un numero entero")
        op = valid_menu(menu)
    except:
        print("Error desconocido")
        op = valid_menu(menu)
    finally:
        return op

def archivos():
    while True:
        menu_a = '''Menu Archivos:
1. Obtener datos a traves de la API
2. Guardar datos de pokemon en excel
3. Obtener datos de un pokemon
4. Regresar al menu principal'''
        op = valid_menu(menu_a)
        if op == 1:
            api_call()
        elif op == 2:
            guardarExcel()
        elif op == 3:
            datos_poke()
        elif op == 4:
            break
        else:
            print("Error: Favor de solo ingresar opciones que estan en el menu")

def graficas():
    while True:
        menu_g = '''Menu Graficas:
1. Graficar stats de un pokemon
2. Graficar promedio de stats en un tipo
3. Graficar cuantos pokemon hay por tipo
4. Regresar al menu principal'''
        op = valid_menu(menu_g)
        if op == 1:
            graf_stats()
        elif op == 2:
            graf_promedio_tipo()
        elif op == 3:
            graf_tipos()
        elif op == 4:
            break
        else:
            print("Error: Favor de solo ingresar opciones que estan en el menu")

def calculos():
    while True:
        menu_c = '''Menu Calculos:
1. Contar cuantos pokemon hay de un tipo dado
2. Calcular promedios de un tipo de pokemon
3. Imprimir los pokemones con mas hp de todos los tipos
4. Regresar al menu principal'''
        op = valid_menu(menu_c)
        if op == 1:
            pokemon_tipo()
        elif op == 2:
            promedio_tipo()
        elif op == 3:
            mejorPokemonPorTipo()
        elif op == 4:
            break
        else:
            print("Error: Favor de solo ingresar opciones que estan en el menu")

#Flujo Principal
while True:
    menu_p = '''Menu Principal:
1. Lectura/Escritura de archivos
2. Graficas
3. Calculos matematicos
4. Salir'''
    op = valid_menu(menu_p)
    if op == 1:
        archivos()
    elif op == 2:
        graficas()
    elif op == 3:
        calculos()
    elif op == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Error: Favor de solo ingresar opciones que estan en el menu")
