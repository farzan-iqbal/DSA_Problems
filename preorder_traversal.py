# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        result = []

        def helper(node):
            if not node:
                return
            result.append(node.val)    # root
            helper(node.left)          # left
            helper(node.right)         # right

        helper(root)
        return result
