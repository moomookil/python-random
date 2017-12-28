# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:13:11 2017

@author: Brian
"""

with open("C:/Users/Brian/Documents/CST480-python/place.txt", "r") as myfile:
    count_chicago = 0
    count_boston = 0
    count_seattle = 0
    for line in myfile:        
        for word in line.split():  
            if word == "Chicago":
                count_chicago += 1
            elif word == "Boston":
                count_boston += 1
            else:
                count_seattle += 1  
    print "found %r Chicago" %count_chicago
    print "found %r Boston" %count_boston
    print "found %r Seattle" %count_seattle
                
#Chicago     """
#Chicago      found 8 Chicago
#Seattle      found 6 Boston
#Seattle      found 10 Seattle
#Seattle     """
#Chicago
#Chicago
#Chicago
#Boston
#Boston
#Boston
#Seattle
#Boston
#Chicago
#Chicago
#Chicago
#Seattle
#Seattle
#Boston
#Boston
#Seattle
#Seattle
#Seattle
#Seattle
        