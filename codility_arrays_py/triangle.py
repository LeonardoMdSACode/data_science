def solution(A):
    # each element of array A is an integer within the range [-2147483648..2147483647].
    for value in A:
     if value < -2147483648 or value > 2147483647:
        print("Value out of range:", value)
        
    # N is an integer within the range [2.. 100,000];
    if len(A) < 0 or len(A) > 100000:
        print("Error: array A must have between 2 and 100000 elements.")

    n = len(A)
    A.sort()
    for i in range(n-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    return 0

print(solution([10, 2, 5, 1, 8, 20]))
print(solution([10, 50, 5, 1]))