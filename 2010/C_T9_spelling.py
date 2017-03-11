#!/usr/bin/python

"""Usage: $ ./google.py inputFile [outputFile]"""

import sys, datetime


def solve(credit, items, price_list):
    """The Latin alphabet contains 26 characters and telephones only have ten digits
       on the keypad. We would like to make it easier to write a message to your 
       friend using a sequence of keypresses to indicate the desired characters.
       The letters are mapped onto the digits as shown below. To insert the character
       B for instance, the program would press 22. In order to insert two characters
       in sequence from the same key, the user must pause before pressing the key a
       second time. The space character ' ' should be printed to indicate a pause. For
       example, 2 2 indicates AA whereas 22 indicates B.
    """

    KEY_MAP = {'a': 2, 'b': 22, 'c': 222,
               'd': 3, 'e': 33, 'f': 333,
               'g': 4, 'h': 44, 'i': 444,
               'j': 5, 'k': 55, 'l': 555,
               'm': 6, 'n': 66, 'o': 666,
               'p': 7, 'q': 77, 'r': 777, 's': 7777,
               't': 8, 'u': 88, 'v': 888,
               'w': 9, 'x': 99, 'y': 999, 'z': 9999}

    price_less_credit = []
    
    for i in range(items):
        value = price_list[i]
        value_less_credit = credit - value
        if value_less_credit > 0:
            price_less_credit.append(value_less_credit)

    for i in price_less_credit:
        try:
            if i in price_list:
                one = i
                one_index = price_list.index(one)
                price_list[one_index] = None
                another = credit - one
                another_index = price_list.index(another)
                
                index = [one_index + 1, another_index + 1]

                return "{} {}".format(min(index), max(index))
        except ValueError:
            pass


def main():
    # Test if at least input file is provided
    if len(sys.argv) < 2:
        print('Please provide input file')
        print('Usage: %s inputfile [outputfile]' % sys.argv[0])
        return
    # Start time
    timestart = datetime.datetime.now()

    # Open input and output files
    try:
        inputFile = open(sys.argv[1])
    except:
        print('Failed to read input file %s' % sys.argv[1])
        return
    try:
        outputFile = open(sys.argv[2], 'w') if len(sys.argv) >= 3 else None
    except:
        print('Failed to create output file %s' % sys.argv[2])
        return

    testCases = int(inputFile.readline().strip())

    # Display number of test cases and output file name 
    print('-----------------')
    print('Test cases: %d ' % testCases)
    print('No output file' if len(sys.argv) < 3 else 'Writing to %s' % sys.argv[2])
    print('-----------------')

    # Loop through all test cases
    for testCaseNumber in range(1, testCases+1):

        # Read an integer
        credit = int(inputFile.readline().strip())
        items = int(inputFile.readline().strip())
        # Read a list of integers
        price_list = list(map(int, inputFile.readline().strip().split()))

        string = 'Case #{}: {}'.format(testCaseNumber, solve(credit, items, price_list))

        # print return string and write it to output file
        print(string)
        if outputFile:
            outputFile.write(string + '\n')

    # Print some final info: output file name and execution time
    print('-----------------')
    print('Written to %s' % sys.argv[2] if outputFile else 'No output file')
    print('Elapsed time: %s' % (datetime.datetime.now() - timestart))
    print('-----------------')

    # Close input and output files
    inputFile.close()
    if outputFile:
        outputFile.close()

if __name__=='__main__':
    main()