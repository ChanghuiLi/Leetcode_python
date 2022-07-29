from typing import *
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(self, root: TreeNode, res: list[int]):
            if not root:
                return
            res.append(root.val)
            preorder(root.left, res)
            preorder(root.right, res)
        res = []
        preorder(root, res)
        return res
    def preorderTraveral(self, root: Optional[TreeNode]) -> List[int]:
        s = []
        res = []
        node = root
        while len(s) > 0 or node:
            while node:
                s.append(node)
                res.append(node.val)
                node = node.left
            temp = s.pop()
            node = temp.right
        return res

    def inorderTraveral(self, root:Optional[TreeNode]) -> List[int]:
        s = []
        res = []
        node = root
        while len(s) > 0 or node:
            while node:
                s.append(node)
                node = node.left
            temp = s.pop()
            res.append(temp.val)
            node = node.right
        return res
# 1,/2,3/,4,5,6,7,/8.9.10.11.12.13.14.15/
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = []
        res = []
        node = root
        pre = None  # 记录上一个访问的节点
        while len(s) > 0 or node:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            if not node.right or node.right == pre:
                res.append(node.val)
                pre = node
                node = None
            else:
                s.append(node)
                node = node.right
        return res
