#!/usr/bin/python
import sys

def is_balanced(start_weight, actions):
    return (0 == eval(start_weight, actions))

def eval(start_wt, actions):
    '''subtract right from left. Return value of Zero is balanced, positive is heavy on the left, negative heavy on the right'''
    left = start_wt
    right = 0
    for power,action in enumerate(actions):
        #print 'power ',power
        w = pow(3, power)
        if action == 'L':
            left = left + w
        elif action == 'R':
            right = right + w
    return left - right

def answer(n=1):
    #actions = list("LR-R")
    actions = list("RLLR")
    w = n
    print 'ST WEIGHT : ',w
    print 'ACTIONS : ',actions
    print 'EVAL -> : ',eval(w,actions)
    


if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1].strip())
        answer(n)
    else:
        print 'Program requires an input weight. Exiting.'
        exit()

