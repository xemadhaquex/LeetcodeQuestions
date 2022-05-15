# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        deepness = 0
        deepest = []
        
        def dfs(root,depth):
            nonlocal deepness, deepest
            
            if root != None:
                if depth == deepness:
                    deepest.append(root.val)
                elif depth>deepness:
                    deepness = depth
                    deepest = []
                    deepest.append(root.val)

                dfs(root.left,depth+1)
                dfs(root.right,depth+1)
        
        dfs(root,0)
        
        return sum(deepest)
                
