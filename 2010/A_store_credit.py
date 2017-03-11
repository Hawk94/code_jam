#!/usr/bin/python

"""Usage: $ python A_store_credit.py inputFile [outputFile]"""

import sys, datetime


def solve(credit, items, price_list):
    """You receive a credit C at a local store and would like to buy two items.
       You first walk through the store and create a list L of all available items.
       From this list you would like to buy two items that add up to the entire value
       of the credit. The solution you provide will consist of the two integers
       indicating the positions of the items in your list (smaller number first).
    """
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