def multiply(A, B):
    m = len(A)
    n = len(B)
    prod = [0] * (m + n - 1)
    for i in range(m):
        for j in range(n):
            
            prod[i + j] += A[i] * B[j]
    print(prod)
A = [5, 0, 10, 6]
B = [1, 2, 4]
multiply(A, B)