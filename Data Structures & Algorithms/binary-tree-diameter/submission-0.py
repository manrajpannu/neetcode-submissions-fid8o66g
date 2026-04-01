# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = [0]

        def heights(root):
            if not root:
                return 0

            left =  heights(root.left)
            right = heights(root.right)

            dia[0] = max(dia[0], left+right)
            print(root.val,left,right)
            return 1 + max(left,right)
        
        heights(root)
        return dia[0]