mi_primer_dict = dict()
print(type(mi_primer_dict))

mi_otro_dict = {}
print(type(mi_otro_dict))

mi_otro_dict = {"nombre": "Leonel", "apellido": "Castillero", "edad": 26, 1: "Python"}

mi_primer_dict = {
"nombre": "Leonel", 
"apellido": "Castillero", 
"edad": 26, 
"lenguaje": {"Python", "Java", "JavaScript"}
}
#un diccionario es una directorio de claves y valores
#un diccionario es como un json
#en un diccionario podriamos tenrer otro diccionario

print(mi_otro_dict)
print(mi_primer_dict)
print(len(mi_otro_dict))

print(mi_primer_dict["nombre"])
#como actualizar una clave
mi_primer_dict["nombre"] = "Juan"
print(mi_primer_dict["nombre"])

#como agregar una clave
mi_primer_dict["nacionalidad"] = "Hondureño"
print(mi_primer_dict)

#como eliminar una clave
del mi_primer_dict["edad"]
print(mi_primer_dict)

print("lenguaje" in mi_primer_dict)
print("Pytho" in mi_primer_dict)
print("Hondureño" in mi_primer_dict)

print(mi_primer_dict.keys())
print(mi_primer_dict.values())
print(mi_primer_dict.items())
print(mi_primer_dict.copy())
print(mi_primer_dict.fromkeys(("nombre", "apellido")))
print(mi_primer_dict)
#otra manera de cear un diccionario
nuevo_dict = dict.fromkeys(("nombre", "apellido"))
print(nuevo_dict)

nuevo_dict = dict.fromkeys(mi_otro_dict)
print(nuevo_dict)

'''nuevo_dict = dict.fromkeys()
print(nuevo_dict)
''' #esto dara error porque no le pasamos ningun iterable

print(tuple(mi_primer_dict))
print(set(mi_primer_dict))

nuevo_mamahuevazooo = dict.fromkeys(mi_primer_dict, 'Mamahuevooo')
print(nuevo_mamahuevazooo)

partes_completadas_de_mi_back = {
    'backend':0,
     'frontend':0,
     'mobile':0, 
     'data':0}
print(partes_completadas_de_mi_back)



back = dict.fromkeys(partes_completadas_de_mi_back, 1)

back['backend'] = 100
back['frontend'] = 100

print(back)

valores = mi_primer_dict.values()
print(list(valores))
print
print(valores)