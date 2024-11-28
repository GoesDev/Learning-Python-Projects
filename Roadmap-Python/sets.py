A = {1, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

# União de A com B
print(A.union(B))
# Ou
print(A | B)

# Pertence ao conjunto A e ao conjunto B
print(A.intersection(B))
# Ou
print(A & B)

# Pertence ao conjunto A e NÃO pertence ao conjunto B
print(A.difference(B))
# Ou
print(A - B)

# Pertence ao conjunto B e NÃO pertence ao conjunto A
print(B.difference(A))
# Ou
print(B - A)

# Itens Únicos do set A e B
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
