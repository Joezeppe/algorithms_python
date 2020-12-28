"""
    - Node: Each circled alphabet represents a node. A node is any structure that holds data.
    - Binary Tree: A binary tree is one in which each node has a maximum of two children.
    - BST or Binary Search Trees: is a binary tree that stores its nodes in such a way
                                  to be able to search through the tree efficiently.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

current = n1
while current:
    print(current.data)
    current = current.left_child


class Tree:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        curr = self.root_node
        while curr.left_child:
            curr = curr.left_child
        return curr

    # O(n) with n being the height of the tree
    def find_max(self):
        curr = self.root_node
        while curr.right_child:
            curr = curr.right_child
        return curr

    # O(n) with n being the height of the tree
    def insert(self, data):
        node = Node(data)
        if not self.root_node:
            self.root_node = node
        else:
            curr = self.root_node
            parent = None
            while True:
                parent = curr
                if node.data < curr.data:
                    curr = curr.left_child
                    if not curr:
                        parent.left_child = node
                        return
                else:
                    curr = curr.right_child
                    if not curr:
                        parent.right_child = node
                        return

    def get_node_with_parent(self, data):
        parent = None
        curr = self.root_node

        if not curr:
            return parent, None,

        while True:

            # breaks the loop if True
            if curr.data == data:
                return parent, curr

            elif curr.data > data:
                parent = curr
                curr = curr.left_child
            else:
                parent = curr
                curr = curr.right_child

        return parent, curr

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if not parent and not node:
            return False

        # get children count
        children_count = 0

        if node.left_child and node.right_child:
            children_count = 2

        elif not node.left_child and not node.right_child:
            children_count = 0

        else:
            children_count = 1

        # node has no children,  just make parent right or left child to none
        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None

        elif children_count == 1:
            # initiate the node's child
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            if parent:
                if parent.right_child is node:
                    parent.right_child = next_node
                if node.left_child is not None:
                    parent.left_child = next_node
            else:
                self.root_node = None

        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child

            node.data = leftmost_node.data

            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):

        curr = self.root_node
        while True:
            if curr is None:
                return None

            elif curr.data is data:
                return data

            elif data < curr.data:
                curr = curr.left_child

            else:
                curr = curr.right_child


if __name__ == "__main__":
    tree = Tree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    tree.insert(9)
    tree.insert(1)
    tree.insert(3)
    # tree.remove(3)

    for i in range(1, 10):
        found = tree.search(i)
        print(f"{i}: {found}")