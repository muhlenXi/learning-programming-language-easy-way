numbers = [2, 8, 7, 6, 4, 1]
numbers1 = []

def bubble(nums):
    count = len(nums)
    if len(nums) <= 0:
        return
    for index in range(count-1):
        maxLength = count-index-1
        for index_j in range(0, maxLength):
            changed = False
            if nums[index_j] > nums[index_j+1]:
                temp = nums[index_j]
                nums[index_j] = nums[index_j+1]
                nums[index_j+1] = temp
                changed = True
            if changed == False:
                break
    return nums

print(bubble(numbers))