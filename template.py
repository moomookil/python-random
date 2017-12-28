# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""
import math
import sys

def solve_quadratic(a,b,c):
    root1 = 0 
    root2 = 0
    q=b*b-4*a*c
    if q<0 :
        print "Root is negative"
        sys.exit()
    denomonator=2*a*c  
    if denomonator ==0:
        print "denomonator is zero"
        sys.exit()
    root1= (-b+math.sqrt(q))/denomonator
    root2= (-b-math.sqrt(q))/denomonator 
    return (root1,root2) 
      
(x,y,z)=(3,10,4)
(a,b)=solve_quadratic(x,y,z)
print "root 1 = ",a

print "root 2 = ",b
              
    