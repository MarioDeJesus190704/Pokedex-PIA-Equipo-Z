def api_call():
    import requests
    import json
    
    with open("datosPokemon.txt", "w") as fo:
        print("Obteniendo datos de 151 pokemon...")
        for i in range(1, 152):
            try:
                r = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(i))
            except:
                print("Problema con la API, favor de conectarse a internet")
                return()
    
            temp = str()
        
            if r.status_code == 200:
                #print(r.status_code)
                pkm = json.loads(r.text)
                for x,y in pkm.items():
                    if x == "abilities":
                        if len(y) > 1:
                            #print(y[0]["ability"]["name"])
                            #print(y[1]["ability"]["name"])
                            temp += (str(y[0]["ability"]["name"]))+","
                            temp += (str(y[1]["ability"]["name"]))+","
                        else:
                            #print(y[0]["ability"]["name"])
                            temp += (str(y[0]["ability"]["name"]))+","
                            temp += ("N/A")+","
                    if x == "height":
                        #print(y)
                        temp += (str(y))+","
                    if x == "id":
                        #print(y)
                        temp += (str(y))+","
                    if x == "name":
                        #print(y)
                        temp += (str(y))+","
                    if x == "stats":
                        for i in range(6):
                            #print(y[i]["stat"]["name"],":",y[i]["base_stat"])
                            temp += (str(y[i]["base_stat"]))+","
                    if x == "types":
                        if len(y) > 1:
                            #print(y[0]["type"]["name"])
                            #print(y[1]["type"]["name"])
                            temp += (str(y[0]["type"]["name"]))+","
                            temp += (str(y[1]["type"]["name"]))+","
                        else:
                            #print(y[0]["type"]["name"])
                            temp += (str(y[0]["type"]["name"]))+","
                            temp += ("N/A")+","
                    if x == "weight":
                        #print(y)
                        temp += (str(y))+","
            temp += "\n"
            fo.write(temp)
        print("Datos obtenidos, regresando al menu...")
                
if __name__ == "__main__":
    api_call()
