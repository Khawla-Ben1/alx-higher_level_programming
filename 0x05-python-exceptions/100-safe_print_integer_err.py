#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Exception: Unknown format code 'd' for object of type '{}'".format(type(value).__name__), file=sys.stderr)
        return False
