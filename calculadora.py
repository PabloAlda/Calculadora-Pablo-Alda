#Calculadora básica realizada sin la ayuda de chatgpt
#Suma
def suma(a, b):
    return a + b

#Resta
def resta(a, b):
    return a - b

#Multiplicación
def multiplicacion(a, b):
    return a * b

#División
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

#Mostrar en pantalla
while True:
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "5":
        print("¡Hasta luego!")
        break
    elif opcion in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Ingrese números válidos.")
            continue

        if opcion == "1":
            resultado = suma(num1, num2)
            print(f"La suma es: {resultado}")
        elif opcion == "2":
            resultado = resta(num1, num2)
            print(f"La resta es: {resultado}")
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
            print(f"La multiplicación es: {resultado}")
        elif opcion == "4":
            resultado = division(num1, num2)
            print(f"La división es: {resultado}")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
