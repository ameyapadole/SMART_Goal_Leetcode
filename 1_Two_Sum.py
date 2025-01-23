def twoSum(nums, target):

    hashset = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashset:
            return [i, hashset[diff]]
        hashset[num] = i 

print(twoSum([2,7,11,15], 9))