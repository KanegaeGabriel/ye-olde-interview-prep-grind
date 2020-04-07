def missingNumber(nums):
    return sum(range(len(nums)+1)) - sum(nums)

print(missingNumber([3, 0, 1])) # 2
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])) # 8