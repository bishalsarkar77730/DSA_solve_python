A = {1, 5, 10, 20, 40, 80}
B = {6, 7, 20, 80, 100}
C = {3, 4, 15, 20, 30, 70, 80, 120}

D = set(A).intersection(set(B))
E = set(D).intersection(set(C))
print(E)
