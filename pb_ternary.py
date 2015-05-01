#!/usr/bin/python
import sys

PLUS="+"
SUB="-"
ZERO="0"

def negate_bt(digits):
    out = []
    for d in digits:
        if d == PLUS:
            out.append(SUB)
        elif d == SUB:
            out.append(PLUS)
        else:
            out.append(ZERO)
    return out

def decimal_to_balanced_ternary(n):
    if n == 0:
        return n
    out = []
    while n != 0:
        r = n % 3
        if r == 0:
            out.append(ZERO)
        elif r == 1:
            out.append(PLUS)
        else:
            out.append(SUB)
            n = n + 1
        n = n // 3

    out.reverse()
    return out

#addition
#   | - | 0 | + |
#----------------
# - | -+| - | 0 |
#----------------
# 0 | - | 0 | + |
#----------------
# + | 0 | + | +-|
#----------------

def add_bt(a,b):
    out = []
    a.reverse()  
    b.reverse()
    if len(b) > len(a):
        tmp = b
        a = b
        b = tmp

    carry = False
    for x in enumerate(a):
        i = a[x] 
        j = b[x]
        if i is not None and j is not None:
            if i == PLUS and j == PLUS and not carry:
                out.append(SUB)
                carry = True
            if i == PLUS and j == PLUS and carry:
                out.append(Plus)
                carry = True
            if i == SUB and j == SUB and not carry:
                out.append(PLUS)
                carry = False
        elif i is None:
            out.append(j)
        elif j is None:
            out.append(i)

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

