#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if j > i and j != 9 and i != 8:
            print("{}{}".format(i, j), end=', ')
print("89")
