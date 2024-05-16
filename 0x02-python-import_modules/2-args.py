#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
import sys

num_arg = len(sys.argv) - 1
if num_arg > 1:
    print("{} arguments:".format(num_arg), end='\n')
elif num_arg == 1
    print("1 argument:")
else:
    print("{} arguments.".format(num_arg), end='\n')
for i in range(num_arg):
    print("{}: {}".format(i + 1, sys.argv[i + 1]), end='\n')

