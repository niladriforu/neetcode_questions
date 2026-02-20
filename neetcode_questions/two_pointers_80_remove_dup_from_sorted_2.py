def remove_duplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    slow = 2
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

#did not work
# def remove_duplicates(nums):
#     if len(nums) <= 2:
#         return len(nums)
#     left = 0
#     count=0
#     for right in range(len(nums)):
#         if nums[left] == nums[right]:
#             continue
#         if nums[left-1] != nums[right] or count ==1:
#
#         else:
#             count+=1
#





nums = [1,1,1,2,2,3]
print(remove_duplicates(nums))
