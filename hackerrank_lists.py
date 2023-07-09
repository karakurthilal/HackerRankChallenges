# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:46:51 2023

@author: Hilal Karakurt
"""

N = int(input())
liste=[]
inputs=[]
for i in range(N):
  a=list(input().split(" "))
  if 'insert' in a :
    index=int(a[1])
    num=int(a[2])
    liste.insert(index, num)
    
  if 'print' in a:
    print(liste)
    
  if 'remove' in a:
    num=int(a[1])
    liste.remove(num)
    
  if 'append' in a:
    num=int(a[1])
    liste.append(num)
    
  if 'sort' in a:
     liste.sort()
     
  if 'pop' in a:
     liste.pop()
     
  if 'reverse' in a:
     liste.reverse()