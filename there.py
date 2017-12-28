# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:13:46 2017

@author: Brian
"""

with open("C:/Users/Brian/Documents/CST480-python/there.txt", "r") as myfile:
    lineNumber = 0
    for line in myfile:
        row = line.split(",")
        print row[3]