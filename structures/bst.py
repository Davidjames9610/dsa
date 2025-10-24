#%%

class Node:
     def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:

    def __init__(self, tree_value=None):
        self.tree = tree_value

    def traverse(self, some_node):

        if some_node is None:
            return
        else:
            if some_node.left is not None:
                self.traverse(some_node.left)
            if some_node.right is not None:
                self.traverse(some_node.right)
            print(some_node.value)

    def insert(self, value):
        """
        insert node - no balancing right now just traverse until
        node end is found
        """

        if self.tree is None:
            self.tree = Node(value)
        else:
            self._insert_node(self.tree, value)

        
    def _insert_node(self, curr_node, value):
        """
        recursive function
        """

        if value < curr_node.value:
            if curr_node.left is None:
                curr_node.left = Node(value)
            else:
                self._insert_node(curr_node.left, value)
        else:
            if curr_node.right is None:
                curr_node.right = Node(value)
            else:
                self._insert_node(curr_node.right, value)

#%%

my_bst = BST()

my_bst.insert(10)
my_bst.insert(8)
my_bst.insert(12)
my_bst.traverse(my_bst.tree)





    







        
# %%
