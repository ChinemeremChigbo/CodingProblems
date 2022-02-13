# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        def dfs(root,stack,explored,finalList):
            stack += [root]
            if root.left and root.left not in explored:     
                return dfs(root.left,stack,explored,finalList)
            elif root.right and root.right not in explored:
                return dfs(root.right,stack,explored,finalList)
            else:
                if not root.left and not root.right and sum([i.val for i in stack]) == targetSum :
                    finalList += [[i.val for i in stack]]
                explored.add(root)
                stack.pop()
                if stack:
                    popped = stack.pop(-1)
                    return dfs(popped,stack,explored,finalList)
                else:
                    return finalList
                
            
        return dfs(root,[],set(),[])