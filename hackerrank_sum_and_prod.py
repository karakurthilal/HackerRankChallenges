# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:00:01 2023

@author: DİGİTAL
"""

import numpy as np
num=list(input().strip(' '))
N=int(num[0])
M=int(num[2])

my_list=[]
for i in range(M):
    num=list(input())
    new =np.array(num)
    num=new[np.logical_not(new == ' ')]
    my_list.append(num)
    
    
my_array=np.array(my_list).astype(int)
hey1=my_array.reshape(N,M)

heys=np.sum(hey1, axis = 0)
print(np.prod(heys,axis=0))