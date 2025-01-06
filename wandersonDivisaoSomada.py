q_teste = int(input())


def escolhe_conjunto(conjunto, mid, soma):
    rigth, left = [], []
    soma_rigth, soma_left, somaGeral = 0, 0, 0
    for num in conjunto:
        if num > mid:
            soma_rigth += num
            rigth.append(num)
        else:
            soma_left += num
            left.append(num)
        somaGeral += num

    if (soma == somaGeral):
        return soma, conjunto

    if abs(soma-soma_rigth) < abs(soma-soma_left):
        return soma_rigth, rigth
    else:
        return soma_left, left


def verificar_elementos_iguais(lista):
    return all(x == lista[0] for x in lista)


for _ in range(q_teste):
    q_numeros, testes_estaticos = map(int, input().split())
    numeros = list(map(int, input().split()))
    for _ in range(testes_estaticos):
        mid = (max(numeros)+min(numeros))//2
        soma = int(input())
        soma_conjunto, conjunto = escolhe_conjunto(numeros, mid, soma)
        while True:
            if soma == soma_conjunto:
                print('Yes')
                break
            elif len(conjunto) == 1 or verificar_elementos_iguais(conjunto):
                print('No')
                break
            else:
                mid = (max(conjunto)+min(conjunto))//2
                soma_conjunto, conjunto = escolhe_conjunto(conjunto, mid, soma)
