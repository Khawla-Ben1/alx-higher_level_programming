#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
import sys

num = 0
for i in range(len(sys.argv) - 1):
    num += int(sys.argv[i + 1])
print(num)
