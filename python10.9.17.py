###Basic filter a csv to an output csv copying selected rows as-is
import csv,gzip

# make the not-a-number constant (without numpy)
NaN=float('NaN')

#Remember that in math, infinite does not equal infinite,thus
         #NaN does not equal NaN. All real numbers equal themselves      
def isNaN (n):
    return n!=n

 #Parsenums (simplified for comma-free required, and only floats desired)
def parseNums(x):
    try:
        return float(x)
    except:
        return NaN

#Take a row (dictionary) and convert a list of named columns from text into floats
def Numify_Columns(Row,Columns):
    for column in Columns:
        Row[column]=parseNums(Row[column])      

         
#################### START
        
#Constants and Globals
count=0
total=0.0        
COLUMNS=["HIGHDEG","INEXPFTE","AVGFACSAL"]
FILE='c:/Users/Brian/Downloads/MERGED2014_15_PP.csv'

data=open(FILE, 'rU')
#Create the reader

def read_funding_data(path):
    with open(path, 'rU') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row
            
school_data=[]
Missing_Salaray_Count=0
for Row in read_funding_data(FILE):
      if Row["STABBR"] == "IL" and Row ["CITY"] == "Chicago":
         Numify_Columns(Row,COLUMNS)       
         if isNaN(Row["AVGFACSAL"]):
            Missing_Salaray_Count=Missing_Salaray_Count+1
         else:   
            school_data.append([Row["INSTNM"],Row["INEXPFTE"],Row["AVGFACSAL"]])

print school_data
print 'The number of rows withoust Salary data was', Missing_Salaray_Count
 
data.close()



