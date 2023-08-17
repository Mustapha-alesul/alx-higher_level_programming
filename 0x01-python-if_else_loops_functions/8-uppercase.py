#!/usr/bin/python3
def uppercase(str):
    m = ""
    for i in str:
        if ord(i) in range(ord('a'), ord('z') + 1):
            m += chr(ord(i) - 32)
        else:
            m += i
    print("{}".format(m))
