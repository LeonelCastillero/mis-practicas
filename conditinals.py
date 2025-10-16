#condicionales 

#estos nos sirven para hacer una funcion en base a el parametro 
mi_condicional = False

#una condicion if siempre se cumple si es verdadera
if mi_condicional:
    print("El condicional es verdadero")

print("la condicion se cumplio")

mi_condicional = 5 * 3

if mi_condicional == 15:
    print("El condicional es verdadero")

if mi_condicional > 20:
    print("El condicional es mayor a 10")
else:
    print("El condicional es menor a 10")

#usar elif para mas de dos opciones
mi_condicional = 5 * 2

if mi_condicional > 10:
    print("El condicional es mayor a 10")
elif mi_condicional == 10:
    print("El condicional es igual a 10")
else:
    print("El condicional es menor a 10")




