preorder_list = []
postorder_list = []
inorder_list = []

class BinaryTree:
    def __init__(self, root_node = None, left_node = None, right_node = None):
        self.root = root_node
        self.left_child = left_node
        self.right_child = right_node

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj
        return

    def set_left(self, left):
        self.left_child = left
        return

    def set_right(self, right):
        self.right_child = right
        return

    def get_root_val(self):
        return self.root

    def preorder(self):
        if self is None:
            return self
            
        preorder_list.append(self.get_root_val())
        if self.get_left_child() is not None:
            self.get_left_child().preorder()
        if self.get_right_child() is not None:
            self.get_right_child().preorder()
        return

    def get_preorder_list(self):
        self.preorder()
        return preorder_list

    def postorder(self):
        if self is None:
            return self
        
        if self.get_left_child() is not None:
            self.get_left_child().postorder()
        if self.get_right_child() is not None:
            self.get_right_child().postorder()
        postorder_list.append(self.get_root_val())

    def get_postorder_list(self):
        self.postorder()
        return postorder_list

    def inorder(self):
        if self is None:
            return self
        
        if self.get_left_child() is not None:
            self.get_left_child().inorder()
        inorder_list.append(self.get_root_val())
        if self.get_right_child() is not None:
            self.get_right_child().inorder()
        return

    def get_inorder_list(self):
        self.inorder()
        return inorder_list


def create_binary_tree(tree_list):
    # Left Child: 2i+1, Right Child: 2i+2, Parent: floor((i-1)/2)
    if tree_list[0] is None:
        return
    node_list = []
    i = 0
    while i < len(tree_list):
        if tree_list[i] is not None:
            try:
                left = tree_list[2*i + 1]
            except IndexError:
                left = None
            try:
                right = tree_list[2*i + 2]
            except IndexError:
                right = None
            node = BinaryTree(tree_list[i], left, right)
            node_list.append(node)
        else:
            node_list.append(None)
        i += 1
    i = 0
    while i < len(node_list):
        if tree_list[i] is not None:
            try:
                left = node_list[2*i + 1]
            except IndexError:
                left = None
            try:
                right = node_list[2*i + 2]
            except IndexError:
                right = None
            node_list[i].set_left(left)
            node_list[i].set_right(right)
        i += 1
    return node_list[0]