class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    # INSERT
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    # SEARCH
    def search(self, value):
        current = self.root
        while current is not None:
            if current.data == value:
                return True
            elif value < current.data:
                current = current.left
            else:
                current = current.right
        return False
    # DELETE
    def delete(self, value):
        self.root = self.delete_node(self.root, value)
    def delete_node(self, node, value):
        if node is None:
            return None
        # Search left
        if value < node.data:
            node.left = self.delete_node(node.left, value)
        # Search right
        elif value > node.data:
            node.right = self.delete_node(node.right, value)
        # Node found
        else:
            # Case 1: No child
            if node.left is None and node.right is None:
                return None
            # Case 2: Only right child
            if node.left is None:
                return node.right
            # Case 3: Only left child
            if node.right is None:
                return node.left
            # Case 4: Two children
            temp = self.find_min(node.right)
            node.data = temp.data
            node.right = self.delete_node(node.right, temp.data)
        return node
    # Find minimum value
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    # INORDER
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)
    # PREORDER
    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    # POSTORDER
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
    # HEIGHT
    def height(self, node):

        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)
    # DEPTH OF A NODE
    def depth(self, value):
        current = self.root
        depth = 0
        while current is not None:
            if current.data == value:
                return depth

            elif value < current.data:
                current = current.left
            else:
                current = current.right
            depth += 1
        return -1
# CREATE BST
tree = BST()
# INSERT
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)
# TRAVERSALS
print("Inorder:")
tree.inorder(tree.root)
print("\nPreorder:")
tree.preorder(tree.root)
print("\nPostorder:")
tree.postorder(tree.root)
# SEARCH
print("\nSearch 40:", tree.search(40))
# DEPTH
print("Depth of 40:", tree.depth(40))
# HEIGHT
print("Height:", tree.height(tree.root))
# DELETE
tree.delete(40)
print("After deleting 40:")
tree.inorder(tree.root)
# DELETE END NODE
tree.delete(80)
print("\nAfter deleting 80:")
tree.inorder(tree.root)