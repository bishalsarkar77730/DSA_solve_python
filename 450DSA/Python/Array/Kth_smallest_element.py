arr = [7, 10, 4, 20, 15]
K = 4
arr.sort()
result = []
for i in range(0, K):
    result.append(arr[i])
print(result[-1:][0])
