def pode_obter_soma(conjunto, soma):
    if soma in conjunto:
        return "Yes"
    if soma > max(conjunto) or soma < min(conjunto):
        return "No"

    mid = (max(conjunto) + min(conjunto)) // 2
    esquerda = [x for x in conjunto if x <= mid]
    direita = [x for x in conjunto if x > mid]

    if soma <= sum(esquerda):
        return pode_obter_soma(esquerda, soma)
    else:
        return pode_obter_soma(direita, soma)


def testes_esteticos(n, q, elementos, somas):
    resultados = []
    for soma in somas:
        resultado = pode_obter_soma(elementos, soma)
        resultados.append(resultado)
    return resultados


q_teste = int(input())

for _ in range(q_teste):
    q_numeros, testes_estaticos = map(int, input().split())
    numeros = list(map(int, input().split()))
    for _ in range(testes_estaticos):
        soma = int(input())
        print(testes_estaticos(q_numeros, testes_estaticos, elementos, somas))
