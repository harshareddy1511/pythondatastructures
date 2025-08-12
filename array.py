#kadanes Algorithm
def max_subarray_sum(nums):
    max_sum = nums[0]     #initialize with the first element
    current_sum =nums[0]   #initialize current susbarray sum
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

#example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("maximum subarray sum;",max_subarray_sum(arr))



    