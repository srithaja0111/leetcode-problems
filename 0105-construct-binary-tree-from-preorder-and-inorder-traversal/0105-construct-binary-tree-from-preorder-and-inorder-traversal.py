# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={}
        for i in range(len(inorder)):
            inorder_map[inorder[i]]=i
        self.pre=0
        def helper(left,right):
            if left>right:
                return None
            rootv=preorder[self.pre]
            self.pre+=1
            root=TreeNode(rootv)
            mid=inorder_map[rootv]
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root
        return helper(0,len(inorder)-1)