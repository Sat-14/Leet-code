# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack1=[root]
        stack2=[]
        while stack1:
            curr=stack1.pop()
            stack2.append(curr.val)

            if curr.left:
                stack1.append(curr.left) 
            if curr.right:
                stack1.append(curr.right)

        return stack2[::-1]               
        