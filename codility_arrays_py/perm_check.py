def solution(A):
  
    # N is an integer within the range [1.. 100,000];
    if len(A) < 1 or len(A) > 100000:
        print("Error: array A must have between 1 and 100000 elements.")

    # each element of array A is an integer within the range [1..1,000000000].
    for value in A:
     if value < 1 or value > 1000000:
        print("Value out of range:", value)     
  
    N = len(A)
    seen = [False] * N
    for a in A:
        if not 1 <= a <= N:
            return 0
        if seen[a-1]:
            return 0
        seen[a-1] = True
    return 1
print(solution([4, 1, 3, 2]))   
print(solution([4, 1, 3]))