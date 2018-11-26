# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:28:50 2018

@author: e0276496
"""
class InputOutString(object):
    def __init__(self):
        self.s = ''
        
    def getString(self):
        self.s = input("please input:")

    def printString(self):
        print (self.s.upper())

# =============================================================================
# strObj = input("please input:")
# =============================================================================
strObj = InputOutString()
strObj.getString()
strObj.printString()