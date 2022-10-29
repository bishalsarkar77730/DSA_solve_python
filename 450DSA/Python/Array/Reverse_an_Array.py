A = [1,2,3,4]
B = len(A)

# inbuilt function method
A.reverse()

# Loop Method
for i in range(B-1,-1,-1):
    print(A[i])

# one liner
print( A[::-1]) 