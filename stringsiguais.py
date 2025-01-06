input()
custo_minimo = bit_anterior = 0

for bit_a, bit_b in zip(input(), input()):
    if bit_b != bit_a != bit_anterior:
        custo_minimo += 1
        bit_anterior = bit_b
    else:
        bit_anterior = 0

print(custo_minimo)
