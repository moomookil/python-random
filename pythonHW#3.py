# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 15:22:48 2017

@author: Brian
"""

import csv,gzip

DATAFILE = 'c:/Users/Brian/Downloads/MERGED2014_15_PP.csv.gz'
NEW_EXCELFILE = 'c:/Users/Brian/Downloads/roose.xls'
with gzip.open(DATAFILE, "rU") as datafile:
    with open(NEW_EXCELFILE, "w") as f1:      
        for lineNo, line in enumerate(datafile, start=0):  
            if lineNo == 0:
                print line
                #f1.write(line)
            elif line.find('Roosevelt University') != -1:
                print line
                #f1.write(line)
                print 'Row Number:', lineNo
                break
                        

datafile.close()
f1.close()