#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    argm = len(argv)

    print("{} argument{}{}".format(argm, "" 
        if argm == 1 else "s", ":" if argm > 0 else "."))

    for i, ar in enumerate(argv, start=1):
        print("{}: {}".format(i, ar))
