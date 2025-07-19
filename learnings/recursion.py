
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left=left
        self.right=right


def build_tree(nodes,f):
    print(f"Nodes is {nodes}")
    val = next(nodes)
    print(f"Val is {val}")
    if val =='x':
        return None
    left = build_tree(nodes,f)
    right = build_tree(nodes,f)
    return Node(f(val),left,right)


if __name__=='__main__':
    input_list = input().split()
    iter_input_list = iter(input_list)
    root = build_tree(iter_input_list,int)
    print(root)


