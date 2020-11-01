#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def helper(root, res):
    if root is not None:
        helper(root.left, res)
        res.append(root.value)
        helper(root.right, res)
def binaryTreeInOrderTraversal(root):
    result = []
    helper(root, result)
    return result
    