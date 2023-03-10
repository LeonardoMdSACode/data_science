def solution(A, K):
    N = len(A)
    if N == 0:  # empty array
        return A
    K = K % N  # normalize K to be within [0, N)
    if K == 0:  # no rotation needed
        return A
    # split the array into two parts
    left = A[-K:]  # last K elements
    right = A[:N-K]  # first N-K elements
    # concatenate the two parts in reverse order
    return left + right

# example usage
A = [3, 8, 9, 7, 6]
K = 3
print(solution(A, K))  # [9, 7, 6, 3, 8]

A = [0, 0, 0]
K = 1
print(solution(A, K))  # [0, 0, 0]