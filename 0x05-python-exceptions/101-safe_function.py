#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (IndexError, ZeroDivisionError):
        if (IndexError("list index out of range")):
            print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        elif (ZeroDivisionError("division by zero")):
            print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
