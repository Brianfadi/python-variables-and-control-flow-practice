def largest_number(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

nums_tuple = (10, 20, 30, 40, 50)
print(largest_number(nums_tuple))
