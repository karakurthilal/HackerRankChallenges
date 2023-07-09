# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:24:25 2023

@author: DİGİTAL
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import sys 

num=list(input().split(' '))
try:
    n=int(num[0])
    while not (1 <= n <= 10000):
        n = int(input("Invalid input! Enter a number between 1 and 10000: "))
    m=int(num[1])
    while not (1 <= m <= 100):
        m = int(input("Invalid input! Enter a number between 1 and 100: "))


    yeni = defaultdict(list)
    for i in range(n):
        new=input().strip()
        yeni['A'].append(new)


    for i in range(m):
        new1=input().strip()
        yeni['B'].append(new1)



except EOFError:
    sys.exit(0)
indices = []
for word in yeni['B']:
    if word in yeni['A']:
        word_indices = [i+1 for i, w in enumerate(yeni['A']) if w == word]
        indices.append(word_indices)
    else:
        indices.append(-1)

# Print the indices of each occurrence of words in group B in group A
for index in indices:
    if index == -1:
        print(index)
    else:
        print(" ".join(map(str, index)))