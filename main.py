def load_dictionary():
    words = []
    with open('D:\Documents\TERM 6\Data Structures 2\RedBlackTrees\EN-US-Dictionary.txt', 'rt') as myfile:
        for myline in myfile:
            words.append(myline.rstrip('\n'))
    print(words)


#   RED BLACK TREES IMPLEMENTATION : SEARCH - INSERT - PRINT TREE HEIGHT - PRINT TREE SIZE
#   DICTIONARY FUNCTIONS: LOAD DICTIONARY - PRINT SIZE - INSERT A WORD - SEARCH FOR A WORD

if __name__ == '__main__':
    load_dictionary()
    choice  = input('What are you planning to do?')
