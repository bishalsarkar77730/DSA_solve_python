def printFirstRepeating(arr, n):
    k = 0
    max = n
    for i in range(n):
        if (max < arr[i]):
            max = arr[i]
    a = [0 for i in range(max + 1)]
    b = [0 for i in range(max + 1)]
    for i in range(n):
        if (a[arr[i]]):
            b[arr[i]] = 1
            k = 1
            continue
        else:
            a[arr[i]] = i + 1
    if (k == 0):
        print("No repeating element found")
    else:
        min = max + 1
        for i in range(max + 1):
            if (a[i] and (min > (a[i])) and b[i]):
                min = a[i]
        print(arr[min - 1])


arr = [10, 2, 3, 4, 5, 6]
n = len(arr)
printFirstRepeating(arr, n)
