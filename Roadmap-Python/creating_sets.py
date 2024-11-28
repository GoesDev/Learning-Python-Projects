S = set([1, 10, 100])
S.add(5)
S.add(3)
S.remove(3)
S1 = S.copy()
S.clear()

print(S)
print(S1)

for n in S1:
    print(n)
