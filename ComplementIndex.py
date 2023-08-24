'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_dictionary = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in new_dictionary:
                return [new_dictionary[complement],i]
            new_dictionary[num] = i

        return []
solution = Solution()
print(solution.twoSum([3, 2, 4], 6))

ANOTHER SOLUTION:
'''

def twoSum(nums, target):

    hashmap = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in hashmap:
            return [hashmap[difference],i]
        hashmap[nums[i]] = i
    return [-1,-1]

print(twoSum([2,7,11,15],9))