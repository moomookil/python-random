# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:57:55 2017

@author: Brian
"""

import csv,gzip

NaN=float('NaN')
  
def isNaN (n):
    return n!=n

def parseNums(x):
    try:
        return float(x)
    except:
        return NaN

def Numify_Columns(Row,Columns):
    for column in Columns:
        Row[column]=parseNums(Row[column])      
         
chicago_M = 0
chicago_W = 0
newyork_M = 0
newyork_W = 0
cleveland_M = 0
cleveland_W = 0
cincinnati_M = 0
cincinnati_W = 0
atlanta_M = 0
atlanta_W = 0
sanfrancisco_M = 0
sanfrancisco_W = 0
austin_M = 0
austin_W = 0
neworleans_M = 0
neworleans_W = 0
COLUMNS=["HIGHDEG","UGDS","UGDS_MEN","UGDS_WOMEN"]
FILE='c:/Users/Brian/Downloads/MERGED2014_15_PP.csv.gz'

data=open(FILE, 'rU')

def read_funding_data(path):
    with gzip.open(path, 'rU') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row
missing = 0            
school_data={}
for Row in read_funding_data(FILE):
      if Row["STABBR"] == "IL" and Row ["CITY"] == "Chicago":
         Numify_Columns(Row,COLUMNS) 
         if isNaN(Row["UGDS"] or Row["UGDS_MEN"] or Row["UGDS_WOMEN"]):
             missing = missing + 1
         elif Row["HIGHDEG"] >= 2:
             chicago_M = chicago_M + Row["UGDS_MEN"]*Row["UGDS"]
             chicago_W = chicago_W + Row["UGDS_WOMEN"]*Row["UGDS"]
             school_data[Row['CITY']] = [int(chicago_M), int(chicago_W)]
             
      if Row["STABBR"] == "NY" and Row ["CITY"] == "New York":
         Numify_Columns(Row,COLUMNS) 
         if isNaN(Row["UGDS"] or Row["UGDS_MEN"] or Row["UGDS_WOMEN"]):
             missing = missing + 1
         elif Row["HIGHDEG"] >= 2:
             newyork_M = newyork_M + Row["UGDS_MEN"]*Row["UGDS"]
             newyork_W = newyork_W + Row["UGDS_WOMEN"]*Row["UGDS"]
             school_data[Row['CITY']] = [int(newyork_M), int(newyork_W)]
        
      if Row["STABBR"] == "OH" and Row ["CITY"] == "Cleveland":
         Numify_Columns(Row,COLUMNS) 
         if isNaN(Row["UGDS"] or Row["UGDS_MEN"] or Row["UGDS_WOMEN"]):
             missing = missing + 1
         elif Row["HIGHDEG"] >= 2:
             cleveland_M = cleveland_M + Row["UGDS_MEN"]*Row["UGDS"]
             cleveland_W = cleveland_W + Row["UGDS_WOMEN"]*Row["UGDS"]
             school_data[Row['CITY']] = [int(cleveland_M), int(cleveland_W)] 
      
      if Row["STABBR"] == "OH" and Row ["CITY"] == "Cincinnati":
         Numify_Columns(Row,COLUMNS) 
         if isNaN(Row["UGDS"] or Row["UGDS_MEN"] or Row["UGDS_WOMEN"]):
             missing = missing + 1
         elif Row["HIGHDEG"] >= 2:
             cincinnati_M = cincinnati_M + Row["UGDS_MEN"]*Row["UGDS"]
             cincinnati_W = cincinnati_W + Row["UGDS_WOMEN"]*Row["UGDS"]
             school_data[Row['CITY']] = [int(cincinnati_M), int(cincinnati_W)]
             
      if Row["STABBR"] == "TX" and Row ["CITY"] == "Austin":
         Numify_Columns(Row,COLUMNS) 
         if isNaN(Row["UGDS"] or Row["UGDS_MEN"] or Row["UGDS_WOMEN"]):
             missing = missing + 1
         elif Row["HIGHDEG"] >= 2:
             austin_M = austin_M + Row["UGDS_MEN"]*Row["UGDS"]
             austin_W = austin_W + Row["UGDS_WOMEN"]*Row["UGDS"]
             school_data[Row['CITY']] = [int(austin_M), int(austin_W)]
             
      if Row["STABBR"] == "CA" and Row ["CITY"] == "San Francisco":
         Numify_Columns(Row,COLUMNS) 
         if isNaN(Row["UGDS"] or Row["UGDS_MEN"] or Row["UGDS_WOMEN"]):
             missing = missing + 1
         elif Row["HIGHDEG"] >= 2:
             sanfrancisco_M = sanfrancisco_M + Row["UGDS_MEN"]*Row["UGDS"]
             sanfrancisco_W = sanfrancisco_W + Row["UGDS_WOMEN"]*Row["UGDS"]
             school_data[Row['CITY']] = [int(sanfrancisco_M), int(sanfrancisco_W)]
             
      if Row["STABBR"] == "GA" and Row ["CITY"] == "Atlanta":
         Numify_Columns(Row,COLUMNS) 
         if isNaN(Row["UGDS"] or Row["UGDS_MEN"] or Row["UGDS_WOMEN"]):
             missing = missing + 1
         elif Row["HIGHDEG"] >= 2:
             atlanta_M = atlanta_M + Row["UGDS_MEN"]*Row["UGDS"]
             atlanta_W = atlanta_W + Row["UGDS_WOMEN"]*Row["UGDS"]
             school_data[Row['CITY']] = [int(atlanta_M), int(atlanta_W)] 
             
      if Row["STABBR"] == "LA" and Row ["CITY"] == "New Orleans":
         Numify_Columns(Row,COLUMNS) 
         if isNaN(Row["UGDS"] or Row["UGDS_MEN"] or Row["UGDS_WOMEN"]):
             missing = missing + 1
         elif Row["HIGHDEG"] >= 2:
             neworleans_M = neworleans_M + Row["UGDS_MEN"]*Row["UGDS"]
             neworleans_W = neworleans_W + Row["UGDS_WOMEN"]*Row["UGDS"]
             school_data[Row['CITY']] = [int(neworleans_M), int(neworleans_W)]
             
print "Missing Info: ",missing   
print school_data

data.close()
