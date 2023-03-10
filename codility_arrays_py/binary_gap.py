def solution(N):
    # Convert the number to binary representation
    binary = bin(N)[2:]
    
    # Find the starting index of the first one
    start = binary.find('1')
    
    # If there's no one, there's no gap
    if start == -1:
        return 0
    
    # Initialize the maximum gap length
    max_gap = 0
    
    # Iterate over the remaining characters
    for i in range(start+1, len(binary)):
        # If we find another one, we have a new gap
        if binary[i] == '1':
            # Update the maximum gap length if necessary
            max_gap = max(max_gap, i-start-1)
            # Update the starting index for the next gap
            start = i
    
    # Return the maximum gap length
    return max_gap

print(solution(32))