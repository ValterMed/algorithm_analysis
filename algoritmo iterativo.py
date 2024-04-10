def guess_number_iterative(n, x):
    moves = 0
    smallest = 1
    largest = n
    
    while True:
        guess = (smallest + largest) // 2
        if guess == x:
            print(f"Se adivinó el número {x} en {moves} movimientos.")
            return moves
        elif guess < x:
            smallest = guess + 1
        else:
            largest = guess - 1
        moves += 1

#ejemplo de uso del algoritmo iterativo
n = 100
x = 42
print(f"numero de movimientos necesarios para adivinar {x} es: {guess_number_iterative(n, x)}")
