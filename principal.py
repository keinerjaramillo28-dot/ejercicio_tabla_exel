
class principal:
    from usuary import usuario
    from calculadora import calculadora
    from num import numeros
    
    usuario = usuario("jaramillo","1090401071")
    num1 = numeros(7)
    num2 = numeros(10)

    calculadora = calculadora(num1,num2)

    suma = calculadora.suma
    resta=calculadora.resta
    multiplicacio=calculadora.multiplicacion
    division=calculadora.division

    fecha_actual = calculadora.get_fecha()
    fecha_cambiada=calculadora.get_fecha('2025-11-01')

    #mostrar resultado
    print(usuario.mostrar_resultado())
    print(calculadora.mostar_resultao())
    print(num1.mostrar_resultado())
    print(num2.mostrar.resultado())
    print(f"suma: {suma}")
    print(f"resta: {resta}")
    print(f"multiplicacion: {multiplicacio}")
    print(f"divicion: {division}")
    print(f"fecha de la calculadora (antes):{fecha_actual}")
    print(f"fecha de la calculadora (despues):{fecha_cambiada}")
          



    










 