def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
    return L1

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
print(remove_dups(L1, L2))
