class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idxlist = []
        for idx, number in enumerate(nums):
            if target-number in nums:
                idxlist.append(idx)
        return idxlist