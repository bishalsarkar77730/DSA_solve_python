n = 12
# print(int("".join([str(bin(i))[2:] for i in range(1, n + 1)]), 2) % (10 ** 9 + 7))
# string = ""
# for i in range(1, n + 1):
#     string += format(i, "b") # this B comes from format inbuilt function Bin in the Format
# print(int(string, 2) % (10 ** 9 + 7))

limit = 2
current = 1
for i in range(2, n+1):
    if i == limit:
        limit *= 2
        current = ((current * limit) + i) %1000000007
print(current)
