# make the not-a-number constant (without numpy)
import csv, gzip
NaN=float('NaN')
 
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
FILE= 'c:/Users/Brian/Downloads/MERGED2014_15_PP.csv.gz'
count = 0
Columns = ['INEXPFTE']
   #Columns= # .... FILL in 
def read_data(path):
    data=gzip.open(path, 'rU')
    reader = csv.DictReader(data)
    for Row in reader:
        yield Row
sum=0.0       
for Row in read_data(FILE):       
    if Row["STABBR"] == "IL" and Row["CITY"] == "Chicago" and Row["HIGHDEG"] >= "2": 
       Numify_Columns(Row,Columns)
       foo=Row['INEXPFTE']
       count +=1
       sum=sum+foo
average = sum/count
print average
      
data.close()      
       
       
       
            #comput sum and count
                  
#            yield list_of_INEXPFTE
#compute and print average 
            


#data.close()

 
 #print from python the average instructional expense for 4 year schools in chicago
