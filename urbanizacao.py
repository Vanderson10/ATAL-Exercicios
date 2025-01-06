import sys

# Acelera a entrada para evitar Time Limit Exceeded (TLE)
input = sys.stdin.readline

# Início do trecho de código da União-Encontrar (Disjoint Set Union)


class ConjuntoDisjuntoUniao:
    def __init__(self, num_nos: int) -> None:
        # Inicializa cada nó como seu próprio pai para formar conjuntos disjuntos
        self.parent = [*range(num_nos)]
        # Inicializa o tamanho de cada conjunto como 1
        self.size = [1] * num_nos

    def encontrar_pai(self, v: int) -> int:
        # Encontra o representante (pai) do conjunto que contém o nó v
        if self.parent[v] == v:
            return v
        # Compressão de caminho: atualiza o pai de v diretamente para o representante do conjunto
        self.parent[v] = self.encontrar_pai(self.parent[v])
        return self.parent[v]

    def unir(self, a: int, b: int) -> bool:
        # Une os conjuntos que contêm os nós a e b
        a = self.encontrar_pai(a)
        b = self.encontrar_pai(b)
        if a == b:
            # Os nós já estão no mesmo conjunto
            return False
        # Garante que o maior conjunto absorva o menor
        if self.size[a] < self.size[b]:
            a, b = b, a
        # O nó b agora aponta para a como pai
        self.parent[b] = a
        # Atualiza o tamanho do conjunto de a
        self.size[a] += self.size[b]
        return True

    def conectados(self, a: int, b: int) -> bool:
        # Verifica se os nós a e b estão no mesmo conjunto
        return self.encontrar_pai(a) == self.encontrar_pai(b)

# Fim do trecho de código da União-Encontrar


# Lê o número de nós (cidades) e operações da entrada padrão
n, m = map(int, input().split())

# Cria uma instância da União-Encontrar para representar as cidades
cidades = ConjuntoDisjuntoUniao(n)
# Inicializa o tamanho do maior conjunto como 1
tamanho_maior = 1
# Inicializa o número de componentes como o número total de cidades
componentes = n

# Executa m operações de união
for _ in range(m):
    # Lê os pares de cidades e ajusta o índice (base 0)
    a, b = map(lambda i: int(i) - 1, input().split())
    # Se a união for bem-sucedida, reduz o número de componentes
    if cidades.unir(a, b):
        componentes -= 1

    # a é o nó pai após a união na nossa implementação da União-Encontrar
    tamanho_a = cidades.size[cidades.encontrar_pai(a)]
    # Atualiza o tamanho do maior conjunto se necessário
    if tamanho_a > tamanho_maior:
        tamanho_maior = tamanho_a

    # Imprime o número de componentes e o tamanho do maior conjunto
    print(componentes, tamanho_maior)
