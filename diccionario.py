# conjunto de pares de datos
dic={
    "nombre": "hideo kojima",
    "numero": 3134,
    "casado": False,

    123: 88
}
print(dic)
dic["ciudad"]="chiloe"
print(dic)

for key, value in dic.items():
    print(key, value)