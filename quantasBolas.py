def max_bolas_removidas(bolas):
    max_removidas = 0
    while True:
        # Encontrar o primeiro e o último índice de cada cor
        indices = {}
        for i, cor in enumerate(bolas):
            if cor not in indices:
                indices[cor] = [i, i]
            else:
                indices[cor][1] = i

        print("indices:")
        print(indices)

        # Encontrar o par com a maior distância entre os mesmos índices de cor
        max_dist = 0
        for indice in indices.values():
            dist = indice[1] - indice[0]
            if dist > max_dist:
                max_dist = dist
                i, j = indice

        print("maxima distancia:")
        print(max_dist)

        # Se não encontrou nenhum par, termina o loop
        if max_dist == 0:
            break

        # Remove as bolas entre i e j (inclusive)
        bolas = bolas[:i] + bolas[j+1:]
        print("bolas:")
        print(bolas)
        max_removidas += (j - i + 1)
        print("max removidas:")
        print(max_removidas)

    return max_removidas


# Exemplo de uso:
t = int(input())  # Número de casos de teste
for _ in range(t):
    n = int(input())  # Número de bolas
    bolas = list(map(int, input().split()))  # Cores das bolas
    print(max_bolas_removidas(bolas))
