# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:33:39 2017

@author: Brian
"""

import csv

RELAFFIL_FILE = 'c:/Users/Brian/Downloads/RELAFFIL.csv'

def read_funding_data(path):
    with open(path, 'rU') as data:    
        reader = csv.DictReader(data)
        for row in reader:
            yield row  
      
count_episcopal = 0
count_baptist = 0
RELAFFIL = {}
for row in read_funding_data(RELAFFIL_FILE):   
    for word in row['name'].split():          
        if word == 'Episcopal':
            count_episcopal += 1      
            print count_episcopal, 'Episcopal'
        elif word == 'Baptist':
            count_baptist += 1
            print count_baptist, 'Baptist'

if count_episcopal > count_baptist:
    print 'There are more Episcopal than Baptist'
elif count_episcopal < count_baptist:
    print 'There are more Baptist than Episcopal'   
else:
    print 'There are equal numbers of Episcopal and Baptist'
        
#1 Episcopal
#1 Baptist
#2 Baptist
#2 Episcopal
#3 Episcopal
#3 Baptist
#4 Baptist
#4 Episcopal
#5 Episcopal
#5 Baptist
#6 Baptist
#There are more Baptist than Episcopal        
            
         
