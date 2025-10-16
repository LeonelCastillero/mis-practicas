"""
una tupla es una estructura de datos inmutable
en Python que puede contener múltiples elementos.
tambien es un conjunto de valores 
"""

mi_primer_tupla = tuple()
mi_otra_tupla = ()

mi_primer_tupla = (26, 1.70, 'Leonel', 'Castillero')

print(type(mi_primer_tupla))

print(mi_primer_tupla[0])   # Acceder al primer elemento de la tupla
print(mi_primer_tupla[-4])  # Acceder al primer elemento usando indice negativo
#todo es en base al index, si rebasamos el index nos dara error

# con el . accedemos a las operaciones que podemos hacer con las tuplas

print(mi_primer_tupla.count('Leonel')) # cuenta cuantas veces aparece el elemento en la tupla
print(mi_primer_tupla.index(1.70))     # devuelve el index del elemento que le pasemos

#mi_primer_tupla[1] = 1.75  # esto dara error porque las tuplas son inmutables

mi_tupla_adicional = (True, 'Python', -7) # podemos crear tuplas con diferentes tipos de datos

mi_tupla_con_tuplas = (mi_primer_tupla, mi_tupla_adicional) # podemos crear tuplas que contengan otras tuplas

print(mi_tupla_con_tuplas)

print(mi_primer_tupla[0:3]) # podemos hacer slicing en las tuplas, que es como obtener las que queramos

#como hacer una tupla mutable

mi_primer_tupla = list(mi_primer_tupla) # convertimos la tupla en una lista
print(type(mi_primer_tupla))
mi_primer_tupla[1] = 1.75  # ahora si podemos modificar el elemento
print(mi_primer_tupla)
mi_primer_tupla = tuple(mi_primer_tupla) # convertimos la lista de nuevo en una tupla
print(type(mi_primer_tupla))
#en resumen las tuplas son inmutables, pero podemos hacerlas mutables convirtiendolas en listas

del mi_primer_tupla # podemos eliminar una tupla completa con del
print(mi_primer_tupla) # esto dara error porque la tupla ya no existe`