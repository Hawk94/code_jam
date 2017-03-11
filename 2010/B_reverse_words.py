#!/usr/bin/python

"""Usage: $ ./{filename}.py inputFile [outputFile]"""

import sys, datetime


def solve(word_list):
    """Given a list of space separated words, reverse the order of the words.
       Each line of text contains L letters and W words. A line will only consist
       of letters and space characters. There will be exactly one space character
       between each pair of consecutive words.
    """

    word_list.reverse()
    return " ".join(word_list)


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

        # Read a list of integers
        word_list = list(map(str, inputFile.readline().strip().split()))

        string = 'Case #{}: {}'.format(testCaseNumber, solve(word_list))

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