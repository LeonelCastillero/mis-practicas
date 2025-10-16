# class camelCase:


# class snake_case:


# class PascalCase:

# para las clases usamos pascal case

class Celular():
    marca = "Apple"
"""objeto>>>>""" 
    modelo = "16 pro max" """<<<< instancia del objeto"""
    camara = "48mpx" #defenimos atributos

    celular1 = Celular() #instanciamos un objeto

    print(celular1.marca) #accedemos a los atributos

class Celular1:
    def __init__(self, marca, modelo, camara): #metodo constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara #self es como si se estuviera llamando a la clase

        celular2 = Celular1("Samsung", "S23 ultra", "200mpx") #instanciamos un objeto