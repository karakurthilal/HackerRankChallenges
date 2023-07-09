# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:12:19 2023

@author: DİGİTAL
"""

import numpy as np
my_list=[]
count=0
while(True):
    num=list(input())
    new =np.array(num)
    num=new[np.logical_not(new == ' ')]
    my_list.append(num)
    count+=1
    if num[1]=='0':
        break
    else:
        continue
my_array=np.array(my_list).astype(int)
hey1=my_array.reshape(count,2)

hey=np.min(hey1, axis = 1)
  
print(np.max(hey))