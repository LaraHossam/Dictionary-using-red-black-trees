# Dictionary-using-red-black-trees

In order to ensure that the height of the tree remains O(log n) after every insertion abd deletion, 
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
1. **Search** : 
2. **Insertion** :
3. **Deletion** :
4. **Print Tree Height** :
5. **Print Tree size** : 

## Application:   ENGLISH DICTIONARY BASED ON RED-BLACK TREES IMPLEMENTATION
1. **Load Dictionary** :
2. **Print Dictionary size**:
3. **Insert Word** :
4. **Look-up a Word** :
5. **Delete a word**:
