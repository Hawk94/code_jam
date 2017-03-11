"""Utilities for use in Google Code Jam Problems"""

SMALL_IN = 'A-small-practice.in'
LARGE_IN = 'A-large-practice.in'

def read_input(filename):
    """Return a Code Jam input file as a list of lists."""
    in_file = open(filename)
    reader = in_file.read()
    # split file on \n character
    split = reader.split('\n')
    # split file on spaces to get value lists
    value_list = [values.split(' ') for values in split]
    number_of_cases = value_list.pop(0)
    return number_of_cases, value_list


def write_output(output, filename):
    """Save the solution to a Code Jam problem as a .in file."""


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options