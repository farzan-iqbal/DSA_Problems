# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    # Helper to go as left as possible
    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Top of stack is the next node
        top_node = self.stack.pop()
        val = top_node.val
        # If right child exists, push its leftmost path
        if top_node.right:
            self._leftmost_inorder(top_node.right)
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()