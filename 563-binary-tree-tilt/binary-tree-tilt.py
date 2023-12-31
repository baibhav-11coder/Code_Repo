# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findTilt(self, root: Optional[TreeNode]) -> int:
    ans = 0

    def summ(root: Optional[TreeNode]) -> None:
      nonlocal ans
      if not root:
        return 0

      l = summ(root.left)
      r = summ(root.right)
      ans += abs(l - r)
      return root.val + l + r

    summ(root)
    return ans
