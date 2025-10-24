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

    def search(self, some_node, value):

        if some_node is None:
            return False
        if some_node.value == value:
            return True
        elif value < some_node.value:
            return self.search(some_node.left, value)
        else:
            return self.search(some_node.right, value)
        
    def delete(self, value):
        # this confuses me
        
        if self.tree is None:
            return False
        
        found_node = self.find_node(self.tree, value)

        if found_node is not None:
            return False
        else:
            print('found node!', found_node.value)
            return True

    def find_node(self, some_node, value):

        if some_node.value is None:
            return None
        if some_node.value == value:
            return some_node
        if value < some_node.value:
            if some_node.left is None:
                return None
            else:
                return self.find_node(some_node.left, value)
        else:
            if some_node.right is None:
                return None
            else:
                return self.find_node(some_node.right, value)
        

#%%

my_bst = BST()

my_bst.insert(10)
my_bst.insert(8)
my_bst.insert(12)
my_bst.insert(20)
my_bst.insert(16)
my_bst.traverse(my_bst.tree)
my_bst.search(my_bst.tree, 8)

my_bst.delete(8)

"""
                8
        4               12
    2       6       10          20
1         5       8    11          23     

case 1:
    remove 4
    find left most child for right child

case 2:
    remove 12
        option 1: get left most child in right child
        option 2: get right most child in left child

case 3:
    remove 6
        has left child but no right child
        set parant right to child.left
        (would have to compare parant and delete value)

case 4:
    remove 20:
        has right child no left child
        parent right = delete.right
"""






    







        
# %%
