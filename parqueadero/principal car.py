from usuary2 import usuario
from car import Carro
from parking import parqueadero


print("------ de parqueadero------")

cedula = input("Ingrese su cedula: ")
nombre = input("Ingrese su nombre: ")
rango = input("Ingrese su rango: (admin/cliente): ")
usuario = usuario(cedula, nombre, rango)

Placa = input("Ingrese la placa del carro: ")
color = input("Ingrese el color del carro: ")
marca = input("Ingrese la marca del carro: ")
carro = Carro(Placa, color, marca)

parkeo = parqueadero(usuario, carro)
parkeo.registrar_entrada("", "")

opcion = input("¿Desea registrar la salida? (si/no): ")
if opcion == "si":
    parkeo.registrar_salida()
    parkeo.imprimir_informacion()
