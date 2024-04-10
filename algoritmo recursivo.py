def guess_number_recursive(n, x, smallest=1, largest=None, moves=0):
    if largest is None:
        largest = n
        
    guess = (smallest + largest) // 2
    if guess == x:
        print(f"Se adivinó el número {x} en {moves} movimientos.")
        return moves
    elif guess < x:
        return guess_number_recursive(n, x, guess + 1, largest, moves + 1)
    else:
        return guess_number_recursive(n, x, smallest, guess - 1, moves + 1)

#ejemplo de uso del algoritmo recursivo
n = 100
x = 42
print(f"numero de movimientos necesarios para adivinar {x} es: {guess_number_recursive(n, x)}")
