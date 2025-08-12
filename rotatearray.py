#rotatearray in python
def rotate_array(nums, k):
    k =k % len(nums)
    return nums[-k:] + nums[:-k]
nums = [1,2,3,4,5,6,7]
k=3
print(rotate_array(nums, k))

