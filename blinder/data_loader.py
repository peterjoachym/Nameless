#functions that loads different data sets from csv file to local_data file 
import csv
from Data import local_data as data

def load_data(csv_file:str,row_index:int , output:list) -> None:
    input_data = csv.reader(open(csv_file,"r")) 

    for row in input_data:
        element = row[row_index]
        output.append(str(element))

