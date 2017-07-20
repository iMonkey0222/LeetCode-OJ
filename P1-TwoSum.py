
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idxlist = []
        for idx, number in enumerate(nums):
            otherNumber = target-number # the other number
            newNumbers = list(nums)     # copy the list nums
            del newNumbers[idx]         # delete the item in new list by index

            if otherNumber in newNumbers:                    
                idxlist.append(idx)
        return idxlist


nums = [3,2,4]
target = 6
result = Solution.twoSum(Solution(),nums, target)
print(result)
