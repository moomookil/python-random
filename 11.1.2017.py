# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 11:19:02 2017

@author: Brian
"""
import sys,csv


NaN=float('NaN')
  
def isNaN (n):
    return n!=n

#recreate the printf function without relying on futurisms
def printf(str, *args):
    sys.stdout.write(str % args)
    #sys.stdout.flush()

#return a subset of a dictionary from a list of desired keys
def getDictCols(dict,cols):
    return {k:dict[k] for k in cols}
    
# make the constant (without numpy)
NaN=float('NaN')
 
 #Parsenums (simplified for comma-free required, and only floats desired)
def parseNums(x):
    try:
        return float(x)
    except:
        return NaN

#Convert all "NULL"s to blanks w/o creating a whole new dictionary
#modify in-place elements of the the dictionary rather than creating a whole new one
#We could have used a dictionary comprehension if we wanted to return a New dictionary
#but that creates a data dependent memory footprint, the cost is a performance hit since
#all cells are updated, even ones that do not need it.
#def Nulls_To_Blanks(row):
#      map(lambda (k,v) : row.update({k:"" if v=="NULL" else v}),dict.iteritems(row))
###This version is better as it does not perform unecessory updates and
###Note the use of filter since map builds a return value that can be prevented with filter and False
def Nulls_To_Blanks(row):
      filter(lambda (k,v) : row.update({k:""}) if v=="NULL" else False ,dict.iteritems(row))      
#This version returns a new copy with values changed as needed
#def Nulls_To_Blanks(Row):
#    return {(k,("" if v=="NULL" else v)) for (k,v) in dict.iteritems(Row)} 

#use parse_Nums to convert a list of named columns into Numbers
def Numify_Columns(Row,Columns):
    for column in Columns:
        Row[column]=parseNums(Row[column])      

NumCols = ['INEXPFTE'
,'SAT_AVG'
,'ADM_RATE'
,'COSTT4_A'
,'UGDS'
,'DEBT_MDN'
]
OutCols=[
'STABBR'
,'INSTNM'
,'INEXPFTE'
,'SAT_AVG'
,'ADM_RATE'
,'COSTT4_A'
,'UGDS'
,'DEBT_MDN'
]


inputFile = 'c:/Users/Brian/Downloads/filter.csv'
data2= open(inputFile, 'rU')

def roosevelt():
    for i,j in enumerate(data2):
        if i == 22:
            line = j.split(',')
            if line[2]:
                return line[2]                  

roose = roosevelt()
reader2 = csv.DictReader(data2)
NEWFILE = 'c:/Users/Brian/Downloads/filter2.csv'
data_out2=open(NEWFILE,'wb')
#dw = csv.DictWriter(data_out, delimiter=',',quoting=csv.QUOTE_MINIMAL, fieldnames=reader.fieldnames)
nw = csv.DictWriter(data_out2, delimiter=',',quoting=csv.QUOTE_MINIMAL,fieldnames=OutCols )
nw.writer.writerow(nw.fieldnames)
for idx,Row in enumerate (reader2):
    Numify_Columns(Row,NumCols)
    print Row
  #  if roose >= Row['INEXPFTE'] * .9 and roose <= Row['INEXPFTE'] * 1.1:
   #     print Row['STABBR'],Row['INSTNM'],Row['INEXPFTE'],Row['SAT_AVG'],Row['ADM_RATE'],Row['COSTT4_A'],Row['UGDS'],Row['DEBT_MDN']