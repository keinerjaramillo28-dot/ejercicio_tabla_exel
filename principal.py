from vegetales import cebolla, tomate, pasta
from herramientas import cuchillo, olla
from cocina_a import cocina

def verificar_inventario():
    print("Entré a la verificación")

    vegetales = ["Olla", "Cuchillo", "Cebolla", "Tomate", "Pasta", "Agua"]

    for item in vegetales:  # Cambié el nombre para no sobrescribir la lista
        while True:
            respuesta = input(f"¿Tienes {item}? (si/no): ").lower()
            if respuesta == "si":
                break
            elif respuesta == "no":
                print(f"No tienes {item}. No puedes continuar.")
                return False

    print("Inventario completo. ¡Puedes comenzar!")
    return True
    

def juego():
    if not verificar_inventario():
        return

    # Crear objetos correctamente con parámetros si los requieren
    mi_pasta = pasta()
    mi_olla = olla()
    mi_cuchillo = cuchillo(filo=100)  
    mi_cebolla = cebolla()
    mi_tomate = tomate()
    agua = True

    print("lugar de batalla: COCINA")

    # Cortar cebolla
    while not mi_cebolla.esta_muerta():  # Ahora existe el método esta_muerta()
        accion = input("¿Qué quieres hacer? (1-cortar/2-afilar cuchillo): ")
        if accion == "1":
            mi_cuchillo.usar(mi_cebolla)
            mi_cebolla.mostrar_vida()
            if mi_cebolla.esta_muerta():
                mi_cebolla.morir()
        elif accion == "2":
            mi_cuchillo.afilar()
        
    # Cortar tomate
    while not mi_tomate.esta_muerta():
        accion = input("¿Qué quieres hacer? (1-cortar/2-afilar cuchillo): ")
        if accion == "1":
            mi_cuchillo.usar(mi_tomate)
            mi_tomate.mostrar_vida()
            if mi_tomate.esta_muerta():
                mi_tomate.morir()
        elif accion == "2":
            mi_cuchillo.afilar()
    
    print("Has cortado los ingredientes. Agregando a la olla....")
    

    # Hervir la pasta
    while mi_pasta.get_vida() < 100:
        respuesta = input("¿Quieres hervir la pasta? (s/n): ")
        if respuesta.lower() == "s":
            mi_pasta.hervir()
        elif respuesta.lower() == "n":
            print("No herviste la pasta. Juego terminado.")
            return
    
    print("Combate Culinario completado.")
    print("La pasta ha sido servida con éxito.")


juego()