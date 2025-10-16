#loop while 

mi_bucle = 0

while mi_bucle < 10:
    print(mi_bucle)
    mi_bucle += 1

# a los whiles se les puede agregar un else

'''variable = 0

while variable < 11:
    print(variable)
    variable += 1
else:   
    print("El ciclo ha finalizado")'''

#DENTRO DE UN BUCLE PODEMOS DETENERLO CON UN BREAK
contador = 0
while contador < 30:
    contador += 1
    if contador == 21:
        print('el ciclo ya se termino')
        break
    print(contador)

nuevo_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

for valor in nuevo_dict.values():
    print(valor) #puede iterar las veces que esta un valor dentro del diccionario o tupla o lista
    if valor == "Juan":
        break
        