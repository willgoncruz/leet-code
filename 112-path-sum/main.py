# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSumRecursive(self, root, currentSum, targetSum):
        if root == None:
            return False
        
        currentSum += root.val
        if root.left == None and root.right == None:
            return currentSum == targetSum
        
        return self.pathSumRecursive(root.left, currentSum, targetSum) or self.pathSumRecursive(root.right, currentSum, targetSum)
    
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        if root == None:
            return False
        
        return self.pathSumRecursive(root, 0, targetSum)
