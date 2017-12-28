# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 12:05:38 2017

@author: Brian
"""

import gzip
DATAFILE = 'c:/Users/Brian/Downloads/MERGED2014_15_PP.csv.gz'
NEW_EXCELFILE = 'c:/Users/Brian/Downloads/try1.xls'
with gzip.open(DATAFILE, "rU") as datafile:
    with open(NEW_EXCELFILE, "w") as f1:
        for lineNo, line in enumerate(datafile):
            f1.write(line)
            if lineNo==5:
                break

datafile.close()
f1.close()


# enumerate takes a lists and returns tuples for example
# [a,b,c,d] will become (1,a) (2,b) (3,c)