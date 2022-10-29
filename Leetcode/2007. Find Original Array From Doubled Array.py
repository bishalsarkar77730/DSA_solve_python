changed = [1, 3, 4, 2, 6, 8]
c = Counter(changed)

zeros, m = divmod(c[0], 2)
if m: print()
ans = [0] * zeros

for n in sorted(c.keys()):
    if c[n] > c[2 * n]: print()
    c[2 * n] -= c[n]
    ans.extend([n] * c[n])

print(ans)
