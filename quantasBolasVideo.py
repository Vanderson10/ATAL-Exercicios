t = int(input())
for _ in range(t):
    n = int(input())
    numeros_bolas = list(map(int, input().split()))
    maximo_bolas_removidas = 0
    dic = {}
    for i in range(n):
        temp = maximo_bolas_removidas
        esquerda = n - i
        maximo_bolas_removidas = max(maximo_bolas_removidas, dic.get(
            numeros_bolas[i], 0) - esquerda + 1)
        dic[numeros_bolas[i]] = max(
            dic.get(numeros_bolas[i], 0), temp + esquerda)
    print(maximo_bolas_removidas)
