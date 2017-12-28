# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:29:17 2017

@author: Brian
"""

import csv
###pymotw.com/2/csv/
RELAFFIL_FILE = 'c:/Users/Brian/Downloads/RELAFFIL.csv'

def read_funding_data(path):
    with open(path, 'rU') as data:     #r = read only U = Unicode
        reader = csv.DictReader(data)
        for row in reader:
            yield row  #creats a new thread, spawns a thread and waits
#       data.seek(0)          yield used here will create a generator

RELAFFIL = {}
for row in read_funding_data(RELAFFIL_FILE):
    RELAFFIL[row['code']]=row['category']     #creating a variable RELAFFIL
print RELAFFIL
#print '#############################################'
#RELAFFIL = {}
#for row in read_funding_data(RELAFFIL_FILE):
#    RELAFFIL[row['code']]=row['name']
#print RELAFFIL

