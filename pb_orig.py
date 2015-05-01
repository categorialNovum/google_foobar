#!/usr/bin/python
import sys

def is_balanced(start_weight, actions):
    return (0 == eval(start_weight, actions))

def eval(start_wt, actions):
    '''subtract right from left. Return value of Zero is balanced, positive is heavy on the left, negative heavy on the right'''
    left = start_wt
    right = 0
    for power,action in enumerate(actions):
        w = pow(3, power)
        if action == 'L':
            left = left + w
        elif action == 'R':
            right = right + w
    return left - right

def add_steps(paths):
    out = []
    if len(paths) > 0:
        for p in paths:
            out.append(p + list('L'))
            out.append(p + list('-'))
            out.append(p + list('R'))
    else:
        out.append(list('L'))
        out.append(list('-'))
        out.append(list('R'))

    return out

def bfs_search(start_wt):
    paths = []
    depth = 1
    total = start_wt
    done = False
    while not done:
        for p in paths:
            x = is_balanced(start_wt, p)
            if is_balanced(start_wt, p):
                return p
        paths = add_steps(paths)    
        depth = depth + 1

def answer(n=1):
    w = n
    balance_path = bfs_search(w)
    print 'ANSWER -> ',balance_path
    return balance_path
    


if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1].strip())
        answer(n)
    else:
        print 'Program requires an input weight. Exiting.'
        exit()

