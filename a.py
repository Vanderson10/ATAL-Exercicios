def soma_divisoes(lista):
    resultado = []
    resultado.append(sum(lista))
    meio = (max(lista) + min(lista)) // 2
    esquerda = [elemento for elemento in lista if elemento <= meio]
    direita = [elemento for elemento in lista if elemento > meio]
    if len(esquerda) > 0 and not esquerda == lista:
        resultado += soma_divisoes(esquerda)
    if len(direita) > 0 and not direita == lista:
        resultado += soma_divisoes(direita)
    return resultado


t = int(input())
casos = []
for _ in range(t):
    n, q = map(int, input().split())
    lista = list(map(int, input().split()))
    testes = []
    for _ in range(q):
        teste = int(input())
        testes.append(teste)
    casos.append((lista, testes))

for caso in casos:
    lista = caso[0]
    testes = caso[1]
    resultado = set(soma_divisoes(lista))
    for t in testes:
        if t in resultado:
            print("Yes")
        else:
            print("No")
