usuarios = { }
print(usuarios)

usuarios = {"Chaves" : ["Chaves do 8", "24/11/2022", "Recep_01"],
            "Quico": ["Quico do 9", "22/10/2022", "RaioX_03"]
            }
print(usuarios)

usuarios["Florinda"] = ["Dona Florinda", "24/12/2017", "RaioX_04"]
print(usuarios)

print("###---###")
print(usuarios.get("Chaves"))