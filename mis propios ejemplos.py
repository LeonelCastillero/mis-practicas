#para formar parte de la congregacion

sacado = True
no_sacado = False

if sacado:
    print("no puedes entrar a la congregacion")
else:
    print("puedes entrar a la congregacion")


puntos_necesarios = 40
puntos_obtenidos = 20

if puntos_obtenidos >= puntos_necesarios:
    print("puedes obtener el premio")
else:
    print("no puedes obtener el premio")

edad_minima_para_tomar = 18
tu_edad = 16

if tu_edad >= edad_minima_para_tomar:
    print("puedes tomar")
elif tu_edad >= 15 or tu_edad <= 17:
    print("puedes tomar a escondidas equisde")
else:
    print("no puedes tomar")


"""ingresa_tu_edad = int(input("ingresa tu edad: "))

if ingresa_tu_edad >= 18:
    print("tienes la mayoria de edad")
else:
    print("no tienes la mayoria de edad")
"""
#semaforo
semaforo = input("de que color es el semaforo:  ").lower()

if semaforo == "rojo":
    print("detente")
elif semaforo == "amarillo":
    print("ve bajando la velocidad")
elif semaforo == "verde":
    print("puedes avanzar")
else:
    print("tu eres mamahuevo o queeeee")



