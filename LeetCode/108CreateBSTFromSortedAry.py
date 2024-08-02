# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def createBST(nums, start, end):
            if start > end:
                return None
            med = int (start + end)/2
            root = TreeNode(nums[med])
            root.left = createBST(nums, start, med-1)
            root.right = createBST(nums, med+1, end)
            return root

        return createBST(nums, 0, len(nums)-1)
        