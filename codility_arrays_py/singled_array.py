def solution(A):
    unpaired = 0
    for value in A:
        unpaired ^= value # use bitwise XOR operator to cancel out paired elements
    return unpaired

print(solution([9, 3, 9, 3, 9, 7, 9])) # output: 7