#!/usr/bin.python3

from __future__ import print_function

import sys

def safe_function(fct, *args):
    try:
        result = fxt(*args)

    except Excpetion as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None

    else:
        return result
