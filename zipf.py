#-*- coding:utf8 -*-
'''
Created on 17-11-18

@author: czm
'''
from collections import Counter
import matplotlib.pyplot as plt

"""
Zipf 定律
"""

with open('europarl-v7.tok.en') as fp:
    lines = fp.readlines()

count = Counter([])

for line in lines:
    line = line.strip().split()
    count.update(line)

freq = count.most_common()

zipf = {}

for i in range(1, freq[0][1]+1):
    zipf[i] = 0

freq.reverse()

for data in freq:
    zipf[data[1]] += 1

X = range(1,50)
Y = zipf.values()[0:49]
print Y

plt.plot(X,Y)
plt.show()




















if __name__ == '__main__':
    pass