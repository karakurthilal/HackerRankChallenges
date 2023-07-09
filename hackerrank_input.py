# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 20:14:29 2023

@author: Hilal Karakurt
"""

num=list(input().split(" "))
x=int(num[0])
k=int(num[1])
poly=list(input().split(" "))
polynom=(" ".join(map(str, poly)))    
result=(eval(f'{polynom}'.format(polynom)))

if result==k:
    print(True)
else:
    print(False)