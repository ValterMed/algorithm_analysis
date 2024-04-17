def calcular_sumas():
    # Pedir al usuario el número de casos a evaluar
    num_casos = int(input("¿Cuántos casos quieres evaluar? "))

    for caso in range(1, num_casos + 1):
        print(f"Caso {caso}:")
        
        # Pedir al usuario la cantidad de números a evaluar en este caso
        num_numeros = int(input("Ingrese la cantidad de números a evaluar: "))

        # Pedir al usuario los números para este caso
        numeros = []
        for i in range(num_numeros):
            numero = int(input(f"Ingrese el número {i+1}: "))
            numeros.append(numero)

        # Calcular la suma de los números
        suma = sum(numeros)
        
        # Imprimir el resultado para este caso
        print(f"Resultado para el caso {caso}: {suma}")
        print()


# Llamar a la función principal
calcular_sumas()

