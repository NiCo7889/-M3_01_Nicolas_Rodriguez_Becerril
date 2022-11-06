"""
Ejercicio 1
Creación:
Crea una clase llamada Alumno que tenga los atributos nombre y nota
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
Crear un método llamado calificacion que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota
Experimentación:
Crea algunos alumnos
Prueba a ejecutar el método calificacion de cada objeto que has creado
"""

class Alumno():
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        print("El alumno se ha creado con éxito. ")
    def clasificacion(self):
        if self.nota >= 5:
            print( self.nombre, "está apronado. ")
        else:
            print( self.nombre, "está suspenso. ")

print("\n")
alumno1=Alumno("Carlos", 4)
Alumno.clasificacion(alumno1)
print("\n")
alumno2=Alumno("Marcos",9)
Alumno.clasificacion(alumno2)
print("\n")
alumno3=Alumno("Javier", 7)
Alumno.clasificacion(alumno3)
print("\n")
alumno4=Alumno("Juan",3)
Alumno.clasificacion(alumno4)

      

