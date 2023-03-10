def solution(A):
    
    # N is an integer within the range [1.. 100,000];
    if len(A) < 1 or len(A) > 100000:
        print("Error: array A must have between 1 and 100000 elements.")

    # each element of array A is an integer within the range [-1,000000..1,000000].
    for value in A:
     if value < -1000000 or value > 1000000:
        print("Value out of range:", value)     

    max_value = max(A)
    if max_value < 1:
        return 1
    nums = set(A)
    for i in range(1, max_value+2):
        if i not in nums:
            return i
print(solution([1, 3, 6, 4, 1, 2]))   
print(solution([1, 2, 3]))   
print(solution([-1, -3]))   