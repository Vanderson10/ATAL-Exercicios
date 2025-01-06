numero_elementos, valor_maximo, limite = map(int, input().split())
valores = list(map(int, input().split()))
pesos = list(map(int, input().split()))

valores.append(valor_maximo)

profundidade = [[0 for i in range(505)] for j in range(505)]

for i in range(1, numero_elementos + 1):
    for j in range(0, limite + 1):
        profundidade[i][j] = 1e18
        for q in range(i - 1, -1, -1):
            if i - q - 1 > j:
                break
            profundidade[i][j] = min(profundidade[i][j], profundidade[q]
                                     [j - (i - q - 1)] + ((valores[i] - valores[q]) * pesos[q]))
print(profundidade[numero_elementos][limite])
