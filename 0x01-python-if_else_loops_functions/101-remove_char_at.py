#!/usr/bin/python3
def remove_char_at(k, n):
    if n >= 0 and n < len(k):
        result = ""
        for j in range(len(k)):
            if j != n:
                result += k[j]
        return result
    else:
        return k
