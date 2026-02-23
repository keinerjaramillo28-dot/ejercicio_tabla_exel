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

parqueadero = parqueadero(usuario, carro)
parqueadero.registrar_entrada("", "")

opcion = input("¿Desea registrar la salida? (si/no): ")
if opcion == "si":
    parqueadero.registrar_salida()

    parqueadero.imprimir_informacion()
