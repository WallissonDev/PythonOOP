def numero_perfeito(num):
    perfeito = list()
    for c in range(1, num):
        if num % c == 0:
            perfeito.append(c)
    if sum(perfeito) == num:
        return True
    else:
        return print('Não é um número perfeito!')


# Exemplos de Numeros Perfeitos
numero_perfeito(6)
numero_perfeito(28)
numero_perfeito(496)
numero_perfeito(8128)
# Exemplos de Não Perfeitos
numero_perfeito(5)
numero_perfeito(3)