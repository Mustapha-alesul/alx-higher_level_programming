#!/usr/bin/python3
for ASCII_value in range(ord('a'), ord('z') + 1):
    if ASCII_value != ord('q') and ASCII_value != ord('e'):
        print("{}".format(chr(ASCII_value)), end="")
