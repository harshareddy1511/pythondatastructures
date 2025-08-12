#python program to find the maximum prodect of the array
nums = [2, 3, -2, 4]
current_max = current_min = nums[0]
answer = nums[0]
for num in nums[1:]:
    if num < 0:
        current_max, current_min = current_min, current_max
    current_max = max(num, current_max * num)
    current_min = min(num, current_min * num)
    answer = max(answer, current_max)
print(answer)


     