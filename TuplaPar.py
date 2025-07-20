def tupla_par(*tupla):
    lista_tupla = list()
    for k, v in enumerate(tupla):
        if k % 2 == 0:
            lista_tupla.append(v)
    nova_tupla = tuple(lista_tupla[:])
    print(nova_tupla)
    return nova_tupla


tupla_par('oi','estou', 'estudando','oop')