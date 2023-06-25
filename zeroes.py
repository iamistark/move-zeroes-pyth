def moveZeroes(nums):
    zero_count = 0  # Counter to keep track of the number of zeros encountered
    
    # Iterate through the list and move non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i - zero_count] = nums[i]
        else:
            zero_count += 1
    
    # Fill the remaining positions with zeros
    for i in range(len(nums) - zero_count, len(nums)):
        nums[i] = 0
    
    return nums
