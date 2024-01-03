#creando lista modificable 
lista = ["Francisco Alcaide", "chico francy", True, 1.70]

#creando una tupla (no pueden modificarse)
tupla = ["Francisco Alcaide", "chico francy", True, 1.70]


#esto es valido
lista[3] = "makinon"

#esto no es valido
#lista[3] = "makinon"

#creando un conjunto (set) (EN UN CONJUNTO NO MOSTRARA DATOS DUPLICADOS Y NO PODRA LLAMAR ALGUN ELEMENTO POR SU INDICE)

conjunto = {"Francisco Alcaide", "chico francy", True, 1.70}
#print(conjunto[3]) -> no puede acceder al elemento 



#creando un diccionario (dict)

diccionario = {
    'nombre' : "Francisco alcaide",
    'canal' : "Papikaass",
    'estas_emocionado' : True,
    'altura' : 1.70,
    'dato_duplicado' : "Francisco alcaide",
}

print(diccionario["canal"])
 
 
#diccionario = {
#    0 : "Francisco alcaide",
#    1 : "Papikaass",
#    2 : True,
#    3 : 1.70,
#    4 : "Francisco alcaide",
#}