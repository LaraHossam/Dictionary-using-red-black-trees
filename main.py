def load_dictionary():
    words = []
    with open('D:\Documents\TERM 6\Data Structures 2\RedBlackTrees\EN-US-Dictionary.txt', 'rt') as myfile:
        for myline in myfile:
            words.append(myline.rstrip('\n'))


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




