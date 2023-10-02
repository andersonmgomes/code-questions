# Implement a function to check if a tree is balanced. For the purposes of this question,
# a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
# from the root by more than one.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        repr_str =  str(self.value) + ' (' 
        if self.left:
            repr_str += str(self.left.value)
        else:
            repr_str += 'None'
        repr_str += ')('
        if self.right:
            repr_str += str(self.right.value)
        else:
            repr_str += 'None'
        repr_str += ')'
        return repr_str

def is_balanced(root):
    def check_balance(node):
        if not node:
            print('null node')
            return 0
        print('valid node:', node)
        left_height = check_balance(node.left)
        right_height = check_balance(node.right)
        print('heights', left_height, right_height)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            print('returning -1')
            return -1
        print('returning 2', max(left_height, right_height))
        return 1 + max(left_height, right_height)

    return check_balance(root) != -1

# Test Cases

# 1. Basic Balanced Tree
tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(is_balanced(tree1))  # Expected output: True

# 2. Unbalanced Tree with Left-heavy Skew
tree2 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6)), TreeNode(5)), TreeNode(3))
print(is_balanced(tree2))  # Expected output: False

# 3. Unbalanced Tree with Right-heavy Skew
tree3 = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(5, None, TreeNode(7))))
print(is_balanced(tree3))  # Expected output: False

# 4. Balanced Tree with Multiple Levels
tree4 = TreeNode(1, 
                TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), 
                TreeNode(3, TreeNode(6), TreeNode(7))
               )
print(is_balanced(tree4))  # Expected output: True

# 5. Single Node Tree (Edge Case)
tree5 = TreeNode(1)
print(is_balanced(tree5))  # Expected output: True
