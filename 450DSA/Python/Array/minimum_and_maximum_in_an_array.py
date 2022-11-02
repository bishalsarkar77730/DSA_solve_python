# Given an array A of size N of integers. Your task is to find the minimum 
# and maximum elements in the array.

A = [3, 2, 1, 56, 10000, 167]
N = len(A)

# ---------------------------- USING LOOP METHOD ----------------------
#  First make two blank array with initial value 0 to store the previous data
mini = A[0]
maxi = A[0]

for i in range(N):
    if A[i] < mini:
        mini = A[i]
    if A[i] > maxi:
        maxi = A[i]
print("Minimum Value = ", mini)
print("Maximum value = ", maxi)


# ---------------------------- USING SORT METHOD ----------------------

A.sort()
print("Minimum Value Using Sort = ",A[0])
print("Maximum value Using Sort = ",A[-1])
