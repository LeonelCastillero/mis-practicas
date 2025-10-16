'''
sets

'''
mi_primer_set = set(['Leonel', 26, 1.70, 'Castillero']) # los sets se definen con la funcion set() y se pasan los elementos entre corchetes
# tambien se pueden definir con llaves {}, pero si se definen vacios, se crea un diccionario
mi_otro_set = {}

print(type(mi_primer_set))
print(type(mi_otro_set)) # esto no es un set, es un diccionario vacio

mi_otro_set = {'Leonel', 26, 1.70, 'Castillero'}
print(type(mi_otro_set)) # ahora si es un set

print(len(mi_otro_set)) # los sets no permiten elementos repetidos, por lo que si intentamos agregar un elemento que ya existe, no se agregara

#print(mi_otro_set[1]) # esto dara error porque los sets no son indexados, no podemos acceder a sus elementos por su posicion

mi_otro_set.add('Python') # para agregar un elemento a un set usamos el metodo add
print(mi_otro_set)

#los sets no son ordenados, por lo que el orden de los elementos puede cambiar cada vez que imprimimos el set

mi_otro_set.add('Python') # si intentamos agregar un elemento que ya existe, no se agregara
print(mi_otro_set) #un se no admite repeticiones

print('Castillero' in mi_otro_set) # para verificar si un elemento existe en un set usamos el operador in
print('Java' in mi_otro_set)# devuelve False porque el elemento no existe

mi_otro_set.remove('Castillero') # para eliminar un elemento de un set usamos el metodo remove
print(mi_otro_set)
#mi_otro_set.remove('Java') # si intentamos eliminar un elemento que no existe, dara error

#aqui no hay indices, por lo que no podemos eliminar un elemento por su posicion

#mi_otro_set.clear() # para eliminar todos los elementos de un set usamos el metodo clear
print(mi_otro_set)

#del mi_otro_set # para eliminar un set completo usamos la palabra reservada delete
#print(mi_otro_set) # esto dara error porque el set ya no existe

mi_primer_set = set(['Leonel', 26, 1.70, 'Castillero'])
print(mi_primer_set)
mi_primer_set = list(mi_primer_set) # podemos convertir un set en una lista usando la funcion list()
print(type(mi_primer_set)) 
mi_primer_set = set(mi_primer_set) # y podemos convertir una lista en un set usando la funcion set()

nuevo_set = mi_primer_set.union(mi_otro_set) # para unir dos sets usamos el metodo union()
print(nuevo_set)#recordemos que no acepta repetidos, por eso aunque uni ambos, no se ven dobles resultados

print(mi_primer_set.difference(mi_otro_set)) # para ver la diferencia entre dos sets usamos el metodo difference()
