# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,l):
        if not node:
            return
        self.inorder(node.left,l)
        l.append(node.val)
        self.inorder(node.right,l)

    def build(self,l,le,ri):
        if le > ri:
            return None
        mid = (le+ri)//2
        node = TreeNode(l[mid])
        node.left = self.build(l,le,mid-1)
        node.right = self.build(l,mid+1,ri)
        return node

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l = []
        self.inorder(root,l)
        return self.build(l,0,len(l)-1)