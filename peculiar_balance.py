#!/usr/bin/python
import sys

class Node():
    def __init__(self,weight_val,depth=0,prev_balance=0,drift_ct=0,move=None, parent=None):
        self.weight_val = weight_val
        self.depth = depth
        self.balance = prev_balance
        self.drift_ct = drift_ct
        self.move = move
        self.children = []
        self.parent = parent
        if move == 'L':
            self.balance = self.balance + weight_val
        elif move == 'R':
            self.balance = self.balance - weight_val
        elif move == '-':
            return
        else:
            self.balance = weight_val

        if parent is not None and parent.move == self.move:
            self.drift_ct = parent.drift_ct + 1
        else:
            self.drift_ct = 0

    def add_child(self,weight, move):
        n = Node(weight, self.depth + 1, self.balance, self.drift_ct, move, self) 
        self.children.append(n)

def get_answer_path(node):
    path = []
    while node.parent is not None:
        path.append(node.move)
        node = node.parent
    path.reverse()
    return path

def bfs_search(start_weight):
    drift_threshold = 10
    done = False
    root = Node(start_weight)
    current_level = []
    current_level.append(root)
    while not done:
        for node in current_level:
            if node.balance == 0:
                done = True
                return get_answer_path(node)
        weight = pow(3,node.depth)
        next_level = []
        #if node.drift_ct <= drift_threshold:
        for n in current_level:
            #print 'DRIFT : ',n.drift_ct
            if n.drift_ct <= drift_threshold:
                n.add_child(weight, 'L')
                n.add_child(weight, '-')
                n.add_child(weight, 'R')
            next_level = next_level + n.children
        current_level = next_level

def answer(w=1):
    path = bfs_search(w)
    print path

if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1].strip())
        answer(n)
    else:
        print 'Program requires an input weight. Exiting.'
        exit()

