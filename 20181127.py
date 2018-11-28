# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:39:17 2018

@author: e0276496
"""
# =============================================================================
# import math
# c=50
# h=30
# value=[]
#  
# item=  [x for x in input("please input:").split(',')]
# 
# # =============================================================================
 # l = input("please input:")
 # item = l.split(',')
# # =============================================================================
# for d in item:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# 
# print(','.join(value))
# =============================================================================

input_str=input("please input:")
element=[int(x) for x in input_str.split(',')]
rownum=element[0]
colnum=element[1]
# =============================================================================
# multilist=[[0 for col in range(colnum)] for row in range(rownum)]
# =============================================================================
multilist=[[col*row for col in range(colnum)] for row in range(rownum)]
# =============================================================================
# =============================================================================
#  for row in range(rownum):
#      for col in range(colnum):
#          multilist[row][col]=row*col
# =============================================================================
# =============================================================================
        
print(multilist)