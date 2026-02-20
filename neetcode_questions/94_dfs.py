from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
#values = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

    inorder(root)
    return result


# Example usage
values = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
root = build_tree(values)
print(inorderTraversal(root))  # Output: [4, 2, 6, 5, 7, 9, 1, 3, 8]
