n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    maiorSorte = 0
    digitosSortudos = 0
    for i in range(l, r+1):
        digitos = [int(d) for d in str(i)]
        sorte = max(digitos)-min(digitos)
        if maiorSorte <= sorte:
            maiorSorte = sorte
            digitosSortudos = i

        if sorte == 9:
            break
    print(digitosSortudos)
