"""
Ejercicio 3
Creación
Crea una clase llamada Producto que tenga los atributos codigo, nombre, precio y tipo.
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el producto se ha creado con éxito
Crea el método __str__ para visualizar por pantalla la información de los productos
Experimentación
Crea algunos productos
Prueba a mostrar los datos de algun producto y a modificar algun valor, por ejemplo, prueba a modificar el precio de un producto
"""

class Producto():
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
    def __str__(self):
        return "Código: {}\nNombre: {}\nPrecio: {}\nTipo: {}".format(self.codigo, self.nombre, self.precio, self.tipo)

print("\n")
producto1=Producto(1, "balón", 3, "equipo dportivo")
print(producto1)
print("\n")
producto2=Producto(2, "camiseta", 20, "ropa")
print(producto2)
print("\n")
producto3=Producto(3, "ordenador", 400, "electrónica")
print(producto3)
print("\n")
print("\tCAMBIOS: ")
print("\n")
producto1.codigo=7
print(producto1)
print("\n")
producto3.precio=350
print(producto3)