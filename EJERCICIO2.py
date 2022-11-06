"""
Ejercicio 2
Creación:
Copia el ejercicio anterior y realicemos una modificación:
Junto al método init y calificacion, vamos a crear otro método especial de Python, el método str. Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato:
def __str__(self): return "Lo que quiero mostrar"
Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).
Experimentación:
Implementa el método str y haz que muestre el nombre y la nota del alumno
Crea algun objeto de la clase Alumno
Realiza print de esos objetos para visualizar por pantalla la información del str
"""

class Alumno():
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        print("El alumno se ha creado con éxito. ")
    def clasificacion(self):
        if self.nota >= 5:
            print(self.nombre,"está apronado con un",self.nota)
        else:
            print(self.nombre,"está suspenso cun un",self.nota)
    def __str__(self): 
        return "Alumno:{}\nNota:{}".format(self.nombre,self.nota)


print("\n")
alumno1=Alumno("Carlos", 4)
Alumno.clasificacion(alumno1)
print(alumno1)
print("\n")
alumno2=Alumno("Marcos",9)
Alumno.clasificacion(alumno2)
print(alumno2)
print("\n")
alumno3=Alumno("Javier", 7)
Alumno.clasificacion(alumno3)
print(alumno3)
print("\n")
alumno4=Alumno("Juan",3)
Alumno.clasificacion(alumno4)
print(alumno4)