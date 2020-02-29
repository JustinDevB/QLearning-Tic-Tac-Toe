#!/usr/bin/env python3

import sys

FILENAME = "db.txt"
alpha = 0.5              # learning rate
savekey = None
BOARDSIZE = 9
db = {}

def setup():
    global db

    try:
        fd = open(FILENAME,"r")
        db = readfile(fd)
        fd.close()
    except:
        db = {}

def readfile(fd):

    for line in fd.readlines():
        li = line.rstrip().split(' ')
        db[li[0]] = float(li[1])

    return db

def savefile():
    global db

    with open(FILENAME,"w") as fd:
        for key in db:
            print("{0:s} {1:8.6f}".format(key,db[key]), file=fd)


def getmove(board, who):    # this function will be for O
    global db, savekey

    bcopy = [*board]
    movelist = [x for x in range(BOARDSIZE) if bcopy[x] == 0]
    best = 2.0
    for move in movelist:
        bcopy[move] = 2    # 2 is player O
        bkey = "".join(map(str,bcopy))
        if bkey in db:
            val = db[bkey]
        else:
            val = db[bkey] = 0.5
        if val < best:
            best = val
            bestmove = move
            bestkey = bkey
        bcopy[move] = 0    # 0 is empty
    if savekey:
        db[savekey] = alpha * best + (1 - alpha) * db[savekey]
    savekey = bestkey
    return bestmove

def endgame(result):
    global db, savekey

    qval = (None, 1.0, 0.0, 0.5)[result]
    if savekey:
        db[savekey] = alpha * qval + (1 - alpha) * db[savekey]
    savekey = None
    print('x')
    savefile()

if __name__ == "__main__":

    pass

