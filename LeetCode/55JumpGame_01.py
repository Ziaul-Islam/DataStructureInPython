class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        maxi = len(nums) - 1
        while i < maxi:
            if (i + nums[i]) >= maxi:
                return True
            if (nums[i + nums[i]]) == 0:
                right = (i + nums[i]) - 1
                zeroth = (i + nums[i])
                while (right > -1):
                    if(right + nums[right]) > zeroth:
                        i = right
                        break
                    right -= 1
                if right == -1:
                    return False
            else:
                i = i + nums[i]
        return True
