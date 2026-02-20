from typing import List,Optional
from collections import deque
class TreeNode():
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




# final_node = TreeNode()
# stack implementation . python has stack limit of 1000.
def walk(tree):
    if tree is not None:
        final_node.val = tree.val
        final_node.left = walk(tree.right)
        final_node.right = walk(tree.left)
        # walk(tree.left)
        # walk(tree.right)

def walk2(tree,stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            stack.append(node.right)
            print(node.val)
            stack.append(node.left)

#mytree = Node('A', Node('B',Node('D'),Node('E')), Node('C',Node('F'),Node('G')))
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

# mylist = [ 'A' , 'B' , 'C' , 'D','E','F']
# new_list = build_tree(mylist)
# # print(new_list)
# stack = []
# walk(new_list)
# print('-----')
# walk2(new_list,stack)

def invertTree( root):
    # Base case...
    if root == None:
        return root
    # swapping process...
    root.left, root.right = root.right, root.left
    # Call the function recursively for the left subtree...
    invertTree(root.left)
    # Call the function recursively for the right subtree...
    invertTree(root.right)
    return root  # Return the root...


# [2,1,3]
root = [4,2,7,1,3,6,9]
new_list = build_tree(root)
print(invertTree(new_list))

