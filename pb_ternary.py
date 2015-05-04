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

    #out.reverse()
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

def add_digits(a,b):
    '''add two ternary digits, return the result and any carry'''
    result,carry = 0,0
    if a is not None and b is not None:
        if a == PLUS and b == PLUS:
            result,carry = SUB,PLUS
        elif a == SUB and b == SUB:
            result,carry = PLUS,SUB
        elif a or b == PLUS and a or b == ZERO:
            result = PLUS
        elif a or b == SUB and a or b == ZERO:
            result = SUB
        elif a or b == SUB and a or b == PLUS:
            result = ZERO
    elif a is None:
        return b,carry
    elif b is None:
        return a,carry
    return result,carry

def add_bt(a,b):
    out = []
    carry = 0
    a.reverse()  
    b.reverse()
    #make sure a is the longer sequence
    if len(b) > len(a):
        tmp = b
        a = b
        b = tmp
    #zero pad b until lengths match
    while len(b) < len(a):
        b.append(ZERO)

    for x in range(len(a)):
        i = a[x] 
        j = b[x]
        prev = carry
        #print "I - ",i
        #print "J - ",j
        tmp,carry = add_digits(i,j)
        #print "TMP - ",tmp
        #print "C1 - ",carry
        digit, junk = add_digits(tmp,prev)
        #print "C2 - ",carry
        #print "Digit - ",tmp
        out.append(digit)
    #tack on any left over carry digit
    if carry != ZERO:
        out.append(carry)
    out.reverse()
    return out

def answer(n=1):
    #x = decimal_to_balanced_ternary(n) 
    #neg_x = negate_bt(x)
    #print 'ANSWER -> ',x
    #print 'NEGATIVE -> ',neg_x
    a = 2
    b = 5
    at = decimal_to_balanced_ternary(a)
    bt = decimal_to_balanced_ternary(b)
    result = add_bt(at,bt)
    print "A (",a,") : ",at
    print "B (",b,") : ",bt
    print "RESULT : ",result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1].strip())
        answer(n)
    else:
        print 'Program requires an input weight. Exiting.'
        exit()

