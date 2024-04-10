def encontrar_subconjuntos_contiguos_maximos(conjunto):
    subconjuntos_maximos = []
    maximo_global = [0] * (len(conjunto) + 1)

    for i in range(1, len(conjunto) + 1):
        maximo_local = [0] * (len(conjunto) + 1)
        for j in range(i, len(conjunto) + 1):
            maximo_local[j] = max(maximo_local[j - 1] + conjunto[j - 1], conjunto[j - 1])
            maximo_global[i] = max(maximo_global[i], maximo_local[j])
    
    maximo_global = max(maximo_global)
    
    for i in range(len(conjunto)):
        for j in range(i + 1, len(conjunto) + 1):
            if maximo_global == sum(conjunto[i:j]):
                subconjuntos_maximos.append(conjunto[i:j])

    return subconjuntos_maximos

# Ejemplo de uso
conjunto = [32,23,32,-32434,1,14,34,12,342,124,14,532,523,-643,32,4,43,-6375,23,5,-65334,324,234,234,5,-531246,1,146,1561,13,415,1,-516,514,51,34,-634]
subconjuntos = encontrar_subconjuntos_contiguos_maximos(conjunto)
print("Subconjuntos contiguos máximos:", subconjuntos)