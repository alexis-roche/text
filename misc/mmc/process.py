import math
import numpy as np


def readlines(fname):
    for line in open(fname):
        yield line
    

def end_of_post(line, repeats=3):
    if len(line) < repeats:
        return False
    return min([l == line[0] for l in line[0:repeats]])
    

fname = 'Maddie.txt'

idx = np.where([end_of_post(line) for line in readlines(fname)])[0]

i = 0
buf = []

lines = readlines(fname)


count = 0
f = open('toto0.txt', 'w')
for line in lines:
    if end_of_post(line):
        f.close()
        count = count + 1
        f = open('toto%d.txt' % count, 'w')
    else:
        f.write(line)
f.close()



"""

lines = f.readlines()
f.close()

idx = []
for i in range(len(lines)):
    if end_of_post(lines[i]):
        idx.append(i)

"""
