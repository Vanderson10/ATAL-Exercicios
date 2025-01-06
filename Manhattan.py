def encontrar_ponto_c(x_b, y_b):
    # Calcula a distância de Manhattan de A até B
    distancia_a_b = abs(x_b - 0) + abs(y_b - 0)
    
    # Verifica se a distância de A até B é par, pois precisamos de uma distância inteira de A até C
    if distancia_a_b % 2 != 0:
        return -1, -1  # Retorna -1, -1 se não for possível encontrar um ponto C
    
    # Calcula a metade da distância de A até B
    metade_distancia = distancia_a_b // 2
    
    # Procura por um ponto C que satisfaça as condições
    for x_c in range(metade_distancia + 1):
        for y_c in range(metade_distancia + 1):
            if abs(x_c - 0) + abs(y_c - 0) == metade_distancia and abs(x_c - x_b) + abs(y_c - y_b) == metade_distancia:
                return x_c, y_c
    return -1, -1

# Lê o número de casos de teste
t = int(input())

# Itera sobre cada caso de teste
for _ in range(t):
    x, y = map(int, input().split())
    cx, cy = encontrar_ponto_c(x, y)
    print(cx, cy)
