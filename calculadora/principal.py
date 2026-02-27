import tkinter as Tk
from usuary import usuario
from calculadora import calculadora
from num import numeros

# Crear usuario (puedes poner tus datos)
usuario_obj = usuario("jaramillo", "1090401071")

# Crear ventana
ventana = Tk.Tk()
ventana.title("Operaciones Matemáticas")
ventana.geometry("400x400")

# Labels y entradas
Tk.Label(ventana, text="Digite el primer número:").pack()
entry_num1 = Tk.Entry(ventana)
entry_num1.pack()

Tk.Label(ventana, text="Digite el segundo número:").pack()
entry_num2 = Tk.Entry(ventana)
entry_num2.pack()

resultado_label = Tk.Label(ventana, text="", font=("Arial", 14))
resultado_label.pack(pady=10)

# Función para limpiar entradas y resultados
def limpiar():
    entry_num1.delete(0, Tk.END)
    entry_num2.delete(0, Tk.END)
    resultado_label.config(text="")

# Función para calcular operaciones
def calcular_operacion(op):
    try:
        # Convertir texto a números
        valor1 = float(entry_num1.get())
        valor2 = float(entry_num2.get())
    except ValueError:
        resultado_label.config(text="Por favor ingrese números válidos")
        return

    # Crear objetos numeros con 3 argumentos (según tu clase)
    num1 = numeros(valor1)
    num2 = numeros(valor2)

    # Crear calculadora
    calc = calculadora(num1, num2)

    # Ejecutar operación
    if op == "suma":
        resultado = calc.suma()
        resultado_label.config(text=f"Suma: {resultado}")
    elif op == "resta":
        resultado = calc.resta()
        resultado_label.config(text=f"Resta: {resultado}")
    elif op == "multiplicacion":
        resultado = calc.multiplicacion()
        resultado_label.config(text=f"Multiplicación: {resultado}")
    elif op == "division":
        if valor2 == 0:
            resultado_label.config(text="Error: División por 0")
            return
        resultado = calc.division()
        resultado_label.config(text=f"División: {resultado}")

# Botones
Tk.Button(ventana, text="Sumar", command=lambda: calcular_operacion("suma")).pack(pady=5)
Tk.Button(ventana, text="Restar", command=lambda: calcular_operacion("resta")).pack(pady=5)
Tk.Button(ventana, text="Multiplicar", command=lambda: calcular_operacion("multiplicacion")).pack(pady=5)
Tk.Button(ventana, text="Dividir", command=lambda: calcular_operacion("division")).pack(pady=5)
Tk.Button(ventana, text="Calcular otros números", command=limpiar).pack(pady=10)

ventana.mainloop()



    










 