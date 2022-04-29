def load_dictionary():
    words = []
    with open('D:\Documents\TERM 6\Data Structures 2\RedBlackTrees\EN-US-Dictionary.txt', 'rt') as myfile:
        for myline in myfile:
            words.append(myline.rstrip('\n'))
    print(words)

if __name__ == '__main__':
    load_dictionary()
