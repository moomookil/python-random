# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:01:49 2017

@author: Brian
"""

with open("C:/Users/Brian/Documents/CST480-python/thereoriginal.txt","r") as myfile:
    lineNumber=0
    for line in myfile:
        for word in line.split():
            if word == "there":
                print "found"