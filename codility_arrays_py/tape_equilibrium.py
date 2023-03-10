def solution(A):
    # compute the total sum of the array
    total_sum = sum(A)
    
    # initialize the minimum difference to a large value
    min_diff = float('inf')
    
    # initialize the left sum to zero
    left_sum = 0
    
    # iterate through the array
    for i in range(len(A) - 1):
        # add the current element to the left sum
        left_sum += A[i]
        
        # compute the difference between the left sum and the right sum
        diff = abs(left_sum - (total_sum - left_sum))
        
        # update the minimum difference if necessary
        if diff < min_diff:
            min_diff = diff
    # each element of array A is an integer within the range [-1,000..1,000].
    for value in A:
     if value < -1000 or value > 1000:
        print("Value out of range:", value)
        
    # N is an integer within the range [2.. 100,000];
    if len(A) < 2 or len(A) > 100000:
        print("Error: array A must have between 2 and 100000 elements.")

    # return the minimum difference
    return min_diff

print(solution([3, 1, 2, 4, 3]))