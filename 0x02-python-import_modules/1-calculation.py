#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("{a} + {b} = {}".format(a, b, sum(a, b)), end='\n')
    print("{a} - {b} = {}".format(a, b, sub(a, b)), end='\n')
    print("{a} * {b} = {}".format(a, b, mul(a, b)), end='\n')
    print("{a} / {b} = {}".format(a, b, div(a, b)), end='\n')
