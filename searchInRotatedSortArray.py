class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        target_set = set()

        for i in nums:
            if target in target_set:
                return nums.index(i-1)
            target_set.add(i)
        return -1