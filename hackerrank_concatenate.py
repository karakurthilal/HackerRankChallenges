# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:10:25 2023

@author: DİGİTAL
"""

import numpy as np
# Enter your code here. Read input from STDIN. Print output to STDOUT

num=list(input().strip(' '))
N=int(num[0])
M=int(num[2])
P=int(num[4])
number=[]
for i in range(N):
    a=list(input().strip())
    number.append(a)
numbers=[]
for i in range(M):
    b=list(input().strip())
    numbers.append(b)

new=np.array(number)
liste_temiz =new[np.logical_not(new == ' ')]

new1=np.array(numbers)
liste_temiz1 =new1[np.logical_not(new1 == ' ')]

array1=liste_temiz.reshape(N,P).astype(int)
array2=liste_temiz1.reshape(M,P).astype(int)

concatenated_array = np.concatenate((array1,array2), axis=0)

print(concatenated_array)


