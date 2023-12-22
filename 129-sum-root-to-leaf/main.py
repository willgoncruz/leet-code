# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    values = []
    
    def sumRoot(self, root, value):
        if root == None:
            return
        
        rootValue = value * 10 + root.val
        if root.left == None and root.right == None:
            self.values.append(rootValue)
            return
        
        self.sumRoot(root.left, rootValue)
        self.sumRoot(root.right, rootValue)
        
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.values = []
        self.sumRoot(root, 0)
        return sum(self.values)
