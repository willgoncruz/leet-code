# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    all_paths = []
    
    def pathSumRecursive(self, root, targetSum, path):
        if not root:
            return
        
        path.append(root.val)
        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0:
            self.all_paths.append(path)
            return
        
        self.pathSumRecursive(root.left, targetSum, path[:])
        self.pathSumRecursive(root.right, targetSum, path[:])
        
    
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.all_paths = []
        self.pathSumRecursive(root, targetSum, [])
        return self.all_paths
