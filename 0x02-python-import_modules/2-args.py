#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    le = len(sys.argv ) - 1
    if le == 0:
        print("0 arguments.")
    elif le == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(le))
    for n in range(le):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
