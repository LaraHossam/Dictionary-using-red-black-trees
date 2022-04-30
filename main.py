def load_dictionary():
    words = []
    with open('EN-US-Dictionary.txt', 'rt') as myfile:
        for myline in myfile:
            words.append(myline.rstrip('\n'))

class Node():
    def __init__(self,value):
        self.value=value
        self.parent=None
        self.left=None
        self.right=None
        self.color=1
        #color=1 means red color=0 means black
class RedBlackTree():
    def __init__(self):
        self.Nil=Node(0)
        self.Nil.color=0 #black
        self.Nil.left=None
        self.Nil.rigth=None
        self.root=self.Nil
    def insert(self,key):
        node=Node(key)
        node.left=self.Nil
        node.right=self.Nil
        node.color=1
        y=None
        x=self.root
        while x!=self.Nil:
            y=x
            if node.value<x.value:
                x=x.left
            else:
                x=x.right
        node.parent=y
        if y==None:
            self.root=node
        elif node.value<y.value:
            y.left=node
        else:
            y.right=node

        if node.parent==None:
            node.color=0
            return
        if node.parent.parent==None:
            return
        self.fix_insert(node)











#   RED BLACK TREES IMPLEMENTATION : SEARCH - INSERT - PRINT TREE HEIGHT - PRINT TREE SIZE - DELETE
#   DICTIONARY FUNCTIONS: LOAD DICTIONARY - PRINT SIZE - INSERT A WORD - SEARCH FOR A WORD

if __name__ == '__main__':
    load_dictionary()
    choice = 0
    while int(choice) <= 5:
        choice = input('Welcome! Here are all the possible choices:\n1. Print dictionary size\n2. Insert Word\n3. Look up'
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

