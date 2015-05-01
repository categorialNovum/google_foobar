#!/usr/bin/python
import sys

def negate_bt(digits):
    out = []
    for d in digits:
        if d == "+":
            out.append("-")
        elif d == "-":
            out.append("+")
        else:
            out.append(d)
    return out

def decimal_to_balanced_ternary(n):
    if n == 0:
        return n
    out = []
    while n != 0:
        r = n % 3
        if r == 0:
            out.append("0")
        elif r == 1:
            out.append("+")
        else:
            out.append("-")
            n = n + 1
        n = n // 3

    out.reverse()
    return out

def answer(n=1):
    x = decimal_to_balanced_ternary(n) 
    neg_x = negate_bt(x)
    print 'ANSWER -> ',x
    print 'NEGATIVE -> ',neg_x


if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1].strip())
        answer(n)
    else:
        print 'Program requires an input weight. Exiting.'
        exit()

