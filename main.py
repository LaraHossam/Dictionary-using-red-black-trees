def load_dictionary():
    words = []
    with open('EN-US-Dictionary.txt', 'rt') as myfile:
        for myline in myfile:
            words.append(myline.rstrip('\n'))


class Node():
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
        # color=1 means red color=0 means black


class RedBlackTree():
    def __init__(self):
        self.Nil = Node(0)
        self.Nil.color = 0  # black
        self.Nil.left = None
        self.Nil.rigth = None
        self.root = self.Nil

    def insert(self, key):
        node = Node(key)
        node.left = self.Nil
        node.right = self.Nil
        node.color = 1
        y = None
        x = self.root
        while x != self.Nil:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return
        if node.parent.parent == None:
            return
        self.fix_insert(node)

        # Balancing tree after insertion

    def fix_insert(self, new_node):
        while new_node.parent.color == 1:
            if new_node.parent.parent.right == new_node.parent:
                uncle = new_node.parent.parent.left
                # Parent is the right child of grandparent, and uncle is the left child of grandparent
                if uncle.color == 1:  # Uncle is RED
                    uncle.color = 0
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                else:  # if new_node's parent is red and uncle is BLACK
                    if new_node == new_node.parent.left:
                        # If parent is the right child of grandparent, and new_node is the left child of parent
                        # RIGHT-LEFT case ---> Perform right rotation on parent
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                        # Parent is the right child of grandparent AND new node is the right child of parent
                        # RIGHT-RIGHT case ---> Perform another rotation
                        new_node.parent.color = 0
                        new_node.parent.parent.color = 1
                        self.left_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.right
                # Parent is the left child of grandparent and uncle is the right child
                if uncle.color == 1:  # Uncle is RED
                    uncle.color = 0
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                else:  # If uncle is BLACK
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self.right_rotate(new_node.parent.parent)
            if new_node == self.root:
                break
        self.root.color = 0

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.Nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.Nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # def __print_helper(self, node, indent, last):
    #     if node != self.Nil:
    #         print(indent)
    #         if last:
    #             print("R----")
    #             indent += "     "
    #         else:
    #             print("L----")
    #             indent += "|    "
    #
    #         s_color = "RED" if node.color == 1 else "BLACK"
    #         print(str(node.value) + "(" + s_color + ")")
    #         self.__print_helper(node.left, indent, False)
    #         self.__print_helper(node.right, indent, True)

    def print_in_order(self, new_node):
        if new_node != self.Nil:
            self.print_in_order(new_node.left)
            print(new_node.value)
            self.print_in_order(new_node.right)

    # def print_tree(self):
    #     self.__print_helper(self.root, "", True)

    #   RED BLACK TREES IMPLEMENTATION : SEARCH - INSERT - PRINT TREE HEIGHT - PRINT TREE SIZE - DELETE
    #   DICTIONARY FUNCTIONS: LOAD DICTIONARY - PRINT SIZE - INSERT A WORD - SEARCH FOR A WORD

    def search(self, root, value):
        if root.value == value or root == self.Nil:
            return root
        if value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)


if __name__ == '__main__':
    load_dictionary()
    choice = 33
    RBT = RedBlackTree()
    RBT.insert(20)
    RBT.insert(3)
    RBT.insert(1)
    RBT.insert(4)
    RBT.insert(7)
    RBT.insert(8)
    RBT.insert(9)
    RBT.insert(33)
    RBT.insert(99)
    RBT.print_in_order(RBT.root)


    # found = RBT.search(99)
    # print(found.value)

    while int(choice) <= 5:
        choice = input(
            'Welcome! Here are all the possible choices:\n1. Print dictionary size\n2. Insert Word\n3. Look up'
            'word\n4. BONUS: Delete Word\n5. Exit program\nChoose the desired operation: ')

        if int(choice) == 1:
            print('Dictionary size is: ')
        elif int(choice) == 2:
            word = input('Please enter the word you desire to insert: ')
        elif int(choice) == 3:
            word = input('Please enter the word you desire to look-up: ')
        elif int(choice) == 4:
            word = input('Please enter the word you desire to delete: ')
        elif int(choice) == 5:
            print('Goodbye!')
            quit()
