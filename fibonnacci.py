# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 17:19:09 2017

@author: Brian
"""
x = raw_input("Please think of a number between 0 and 100!")
h = 100
l = 0
ans = (h+l)/2
guess = 0

print ("Is your secret number " + str(ans) + "?")

while guess < 20:
    hint = raw_input("Enter 'h' to indicate the guess is too high."
       "Enter 'l' to indicate the guess is too low." 
       "Enter 'c' to indicate I guessed correctly.")
    if hint == "h":
        ans = (l + ans)//2
        print ans
    elif hint == "l":
        ans = (ans + h)//2
        print ans
    elif hint == "c":
        print "correct",x
    else:
        print "wrong"
    
        
        
        
