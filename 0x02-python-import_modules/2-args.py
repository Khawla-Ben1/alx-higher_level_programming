#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
import sys

num = len(sys.argv) - 1
if num > 1:
    print("{} arguments:".format(num), end='\n')
elif num == 1
    print("1 argument:")
else:
    print("{} arguments.".format(num), end='\n')
for i in range(num):
    print("{}: {}".format(i + 1, sys.argv[i + 1]), end='\n')

