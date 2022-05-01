# Dictionary-using-red-black-trees

In order to ensure that the height of the tree remains O(log n) after every insertion and deletion, 
we can use a special tree called Red-Black Tree, with special properties that ensure that the height
of the tree is always O(log n) and will never reach O(n) even in the worst case.

### Red-Black Trees
A red-black tree is a kind of self-balancing binary search tree. Each node stores an extra bit, which we will call the **color**, _red_ or _black_. The color ensures that the tree remains approximately balanced during _insertions_ and _deletions_. When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties that constrain how unbalanced the tree can become in the worst case.

### Properties of Red-Black Trees
1. Each node is either red or black
2. The root is black. 
3. All nil leaf nodes are black.
4. If a node is red, then both its children are black.
5. All paths from a single node go through the same number of black nodes in order to reach any of its descendant nil nodes.

## Red-Black Trees Implementation in Python
### Class Node and Class Tree
**Code snippets:**
```
class Node():
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
```
**Code snippets:**
```
class RedBlackTree():
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = 0  # black
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
```
1. **Search** : 
**Code snippets:**
```
    def search(self, root, value):
        if root.value == value or root == self.nil:
            return root
        if value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)
```
2. **Insertion** :
**Code snippets:**
```
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
```
### Balancing tree after insertion:
**Code snippets:**
```
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
```
3. **Print Tree Height** :
**Code snippets:**
```
 def height(self,node):
        # Check if the tree is empty
        if node is None:
            return 0
            # Recursively call height of each node
        leftAns = self.height(node.left)
        rightAns = self.height(node.right)
        # Return max(leftHeight, rightHeight) at each iteration
        return max(leftAns, rightAns) + 1

```
4. **Print Tree size** : 
**Code snippets:**
```
 def size(self, node):
        if node is None or node is self.nil:
            return 0
        else:
            return self.size(node.left) + 1 + self.size(node.right)

```

## Application:   ENGLISH DICTIONARY BASED ON RED-BLACK TREES IMPLEMENTATION
1. **Load Dictionary** :
**Code snippets:**
```
def load_dictionary(node):
    with open('EN-US-Dictionary.txt', 'rt') as myfile:
        for myline in myfile:
            node.insert(myline.rstrip('\n'))
```
2. **Print Dictionary size**
3. **Insert Word** 
4. **Look-up a Word** 

