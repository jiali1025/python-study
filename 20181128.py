# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:10:18 2018

@author: e0276496
"""

# =============================================================================
# raw = input("please input:").split(',')
# raw.sort()
# print(','.join(raw))
# =============================================================================

lines = []
while True:
    s = input("please input:")
    if s:
        lines.append(s.upper())
    else:
        break;
        
for sentence in lines:
    print(sentence)