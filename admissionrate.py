# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:03:46 2017

@author: Brian
"""

''' 
Simplified Admission Rate Code
With lots of plotting examples
'''
import csv
import matplotlib.pyplot as plt
from collections import OrderedDict

# make the constant (without numpy)
NaN=float('NaN')
 
 #Parsenums (simplified for comma-free required, and only floats desired)
def parseNums(x):
    try:
        return float(x)
    except:
        return NaN
    
#use parse_Nums to convert a list of named columns into Numbers
def Numify_Columns(Row,Columns):
    for column in Columns:
        Row[column]=parseNums(Row[column])    
 
#Helper function to accumulate row-over-row aggregations into global variables as needed       
def Aggregate(Row):
    ###only update if a row has all info needed:
    ### since we are converting to float, non-numbers become NaNs
    ### a number is equal to itself, a NaN is equal to _nothing_ so use this fact to test for NaN 
    if Row["UGDS_WOMEN"] != Row["UGDS_WOMEN"] or Row["UGDS_MEN"] != Row["UGDS_MEN"] or Row["UGDS"] != Row["UGDS"]:    
        return  ### clean if style
    if Row["UGDS_WOMEN"] +Row["UGDS_MEN"] >1:
        return
    State=Row["STABBR"]    
    StudentCount[State]=StudentCount.get(State,0.0)+Row["UGDS"]    
    Men[State]=Men.get(State,0.0)+Row["UGDS_MEN"]*Row["UGDS"]   
    Women[State]=Women.get(State,0.0)+Row["UGDS_WOMEN"]*Row["UGDS"]   

#read through the file with a _generator_
def read_school_data(path):
    with open(path, 'rU') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row
            
#################### START
#Constants and Globals
FILE='c:/Users/Brian/Downloads/MERGED2014_15_PP.csv'
# number of admitted students
StudentCount = {}
# number of total applicants 
Men = {}
Women = {}
### Computer Averages 
GenderRatios={}


for Row in read_school_data(FILE):
    Numify_Columns(Row,("UGDS_MEN","UGDS_WOMEN","UGDS"))
    Aggregate(Row)
GenderRatios= dict([ (x, Women[x]/(Men[x]))  for x in Men.keys() ])
print GenderRatios


for State in StudentCount.keys():
    print State, "has a ratio of",(Women[State]/StudentCount[State]), (Women[State]+Men[State]),StudentCount[State]


#Show intermediate results
for State in GenderRatios.keys():
    print State, "has a ratio of", GenderRatios[State]
#Sort the list of averages by value then put it into an OrderedDict 
GenderRatios=OrderedDict(sorted(GenderRatios.items(),cmp = lambda x,y: cmp(x[1],y[1])))
print GenderRatios

#Graph it
#http://matplotlib.org/api/pyplot_api.html
#for layouts see http://www.python-course.eu/matplotlib_multiple_figures.php
plt.close('all')
#http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.figure
fig=plt.figure(figsize=(20,20),dpi=100)
fig.set_facecolor('w')
#create a subplot
plt.subplot(111) #plt.subplot(1,1,1)  
#get the current axes for the subplot
ax = plt.gca()
#http://matplotlib.org/mpl_examples/color/named_colors.hires.png
ax.set_axis_bgcolor('cornsilk')
#http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar   
    
plt.bar(range(0,len(GenderRatios)),GenderRatios.values(),width=0.3,color='red')

plt.plot([x+0.1 for x in range(0,len(GenderRatios))],GenderRatios.values())
#Stack Bars
#plt.bar(range(0,len(RateAverages)),[ 1-x for x in RateAverages.values()] ,bottom=RateAverages.values(),width=0.3,color='blue',edgecolor='pink')

#Side-by-side bars 
#plt.bar([x+0.3 for x in range(0,len(RateAverages))],[ 1-x for x in RateAverages.values()] ,width=0.3,color='blue')

#http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xticks
#xticks offset should be 0.1 for single or stacked bars, 0.4 for side-by-side
plt.xticks([x+0.1 for x in range(0,len(GenderRatios))],GenderRatios.keys(),rotation=90, fontsize=8)

#plt.yticks([x/100.0 for x in range(0,100)],fontsize=6)
plt.grid(axis='y',linestyle='solid')
plt.title("State Admission Rates")
plt.show()
plt.savefig("c:/Users/Brian/Downloads/pyplot_save.png")