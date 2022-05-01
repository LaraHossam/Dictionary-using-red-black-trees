import matplotlib.pyplot as plt
from pylab import rcParams


def load_dictionary(node):
    with open('EN-US-Dictionary.txt', 'rt') as myfile:
        for myline in myfile:
            node.insert(myline.rstrip('\n'))


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
        self.nil = Node(0)
        self.nil.color = 0  # black
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, key):
        node = Node(key)
        node.left = self.nil
        node.right = self.nil
        node.color = 1
        y = None
        x = self.root
        while x != self.nil:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
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
        if y.right != self.nil:
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
        if y.left != self.nil:
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

    def print_in_order(self, new_node):
        if new_node != self.nil:
            self.print_in_order(new_node.left)
            print(new_node.value)
            self.print_in_order(new_node.right)

    def search(self, root, value):
        if root.value == value or root == self.nil:
            return root
        if value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

    def size(self, node):
        if node is None or node is self.nil:
            return 0
        else:
            return self.size(node.left) + 1 + self.size(node.right)


    def height(self,node):
        # Check if the tree is empty
        if node is None:
            return 0
            # Recursively call height of each node
        leftAns = self.height(node.left)
        rightAns = self.height(node.right)
        # Return max(leftHeight, rightHeight) at each iteration
        return max(leftAns, rightAns) + 1

def plot_node(node, rb=True, level=1, posx=0, posy=0):
    width = 2000.0 * (0.5 ** level)  # This will be used to space nodes horizontally
    if node.color == 0 or rb == False:
        plt.text(posx, posy, str(node.value), horizontalalignment='center', color='k', fontsize=10)
    else:
        plt.text(posx, posy, str(node.value), horizontalalignment='center', color='r', fontsize=10)

    if node.left:
        px = [posx, posx - width]
        py = [posy - 1, posy - 15]
        if node.left.color == 0 or rb == False:
            plt.plot(px, py, 'k-')
        else:
            plt.plot(px, py, 'r-')
        plot_node(node.left, rb, level + 1, posx - width, posy - 20)

    if node.right:
        plot_node(node.right, rb, level + 1, posx + width, posy - 20)
        px = [posx, posx + width]
        py = [posy - 1, posy - 15]
        if node.right.color == 0 or rb == False:
            plt.plot(px, py, 'k-')
        else:
            plt.plot(px, py, 'r-')


def plot_tree(node, figsize=(10, 6)):
    if node.color == 1:
        rb = False
    else:
        rb = True
    rcParams['figure.figsize'] = figsize
    fig, ax = plt.subplots()
    ax.axis('off')
    plot_node(node, rb)
    plt.title("Visualization of Red Black Tree")
    plt.show()


    #   RED BLACK TREES IMPLEMENTATION : SEARCH - INSERT - PRINT TREE HEIGHT - PRINT TREE SIZE
    #   DICTIONARY FUNCTIONS: LOAD DICTIONARY - PRINT SIZE - INSERT A WORD - SEARCH FOR A WORD
    # create a graphical representation of a binary tree (plot_tree, below, uses plot_node)


if __name__ == '__main__':
    choice = 0
    rbt = RedBlackTree()
    load_dictionary(rbt)
    # rbt.print_in_order(rbt.root)
    # rbt1 = RedBlackTree()
    # people1 = ['Bob', 'Alice', 'Doug', 'Kathy', 'Queen', 'Carol', 'Irene', 'Tom',
    #            'Peter', 'Wanda', 'Yaakov', 'Luis', 'Zandra', 'Ronald', 'Mabel', 'Ursala', 'Eve',
    #            'Frank', 'Ginger', 'Norm', 'Sarah', 'Jeff', 'Vince', 'Howard',
    #            'Oprah']
    # for p in people1:
    #     rbt1.insert(p)
    # plot_tree(rbt1.root, figsize=(14, 4))
    while int(choice) <= 5:
        choice = input(
            'Welcome! Here are all the possible choices:\n1. Print dictionary size\n2. Insert Word\n3. Look up'
            'word\n4. Exit program\nChoose the desired operation: ')
        if choice.isnumeric() is False or int(choice) > 5:
            print('Enter a valid number.')
            choice = 0
        if int(choice) == 1:
            print('Dictionary size is: '+str(rbt.size(rbt.root)))
        elif int(choice) == 2:
            word = input('Please enter the word you desire to insert: ')
            if rbt.search(rbt.root,word.title()) is not rbt.nil:
                rbt.insert(word.title())
                print(word.title() + ' inserted successfully.')
            else:
                print("Can't add a word that's already in the dictionary.")
        elif int(choice) == 3:
            word = input('Please enter the word you desire to look-up: ')
            if rbt.search(rbt.root,word.title()) is not None:
                print('YES, '+word.title()+' exists in the dictionary.')
            else:
                print('NO, '+word.title()+' does not exist in the dictionary.')
        elif int(choice) == 4:
            print('Goodbye!')
            quit()
