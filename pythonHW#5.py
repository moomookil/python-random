# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:17:32 2017

@author: Brian
"""

import csv, gzip

# make the not-a-number constant (without numpy)
NaN=float('NaN')
 
 #Parsenums (simplified for comma-free required, and only floats desired)
def parseNums(x):
    try:
        return float(x)
    except:
        return 0
#Take a row (dictionary) and convert a list of named columns from text into floats
def Numify_Columns(Row,Columns):
    for column in Columns:
        Row[column]=parseNums(Row[column])      
        
count = 0
total = 0.0
COLUMNS=['HIGHDEG','INEXPFTE','AVGFACSAL']
salary = []
inst_expense = []
         
#################### START
#Constants and Globals
FILE='c:/Users/Brian/Downloads/MERGED2014_15_PP.csv.gz'
  #Columns= # .... FILL in 
def read_data(path):
    data=gzip.open(path, 'rU')
#Create the reader
    reader = csv.DictReader(data)
    for Row in reader:
        yield Row
        
for Row in read_data(FILE):
       if Row["STABBR"] == "IL" and Row["CITY"] == "Chicago":
           Numify_Columns(Row,COLUMNS)
           if Row["HIGHDEG"]>=2:
               count = count +1
               total = total + Row['INEXPFTE']
               salary.append(Row['AVGFACSAL'])
               inst_expense.append(Row['INEXPFTE'])
               
                   
Avg = total/count
print "The average is ", Avg

           
#data.close()