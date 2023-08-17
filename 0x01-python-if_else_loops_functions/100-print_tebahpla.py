#!/usr/bin/python3
for ASCII_val in range(ord('z'), ord('a') - 1, -1):
    if ASCII_val % 2 == 0:
        print("{}".format(chr(ASCII_val)), end="")
    else:
        print("{}".format(chr(ASCII_val - 32)), end="")
