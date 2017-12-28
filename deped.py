# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 11:30:12 2017

@author: Brian
"""

import csv,gzip
DATAFILE = 'c:/Users/Brian/Downloads/MERGED2014_15_PP.csv.gz'
with gzip.open(DATAFILE, "rU") as datafile:
    for lineNo, line in enumerate(datafile):
        print line
        if lineNo==1:
            break

datafile.close()


# enumerate takes a lists and returns tuples for example
# [a,b,c,d] will become (1,a) (2,b) (3,c)
