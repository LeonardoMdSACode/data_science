def solution(A):
        # N is an integer within the range [3.. 100,000];
    if len(A) < 3 or len(A) > 100000:
        print("Error: array A must have between 1 and 100000 elements.")

    # each element of array A is an integer within the range [-1,000000..1,000000].
    for value in A:
     if value < -1000 or value > 1000:
        print("Value out of range:", value)     
            
    A.sort()
    n = len(A)
    return max(A[n-1] * A[n-2] * A[n-3], A[0] * A[1] * A[n-1])

print(solution([-3, 1, 2, -2, 5, 6]))