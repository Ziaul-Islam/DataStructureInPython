class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = int (start + end)/2
            if(target == nums[mid]):
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1
        