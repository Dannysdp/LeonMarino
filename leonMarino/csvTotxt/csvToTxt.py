from ast import Num
from codecs import charmap_build
import csv
import numpy as np
import pandas as pd

def main():
    print("Bienvenido al conversor")
    #path = str(input("File path for reading, remember to have the right formating \n:"))
    #path = path[1:len(path)-1]
    path = "D:\Drive\Analisis Trabajos - Copy.csv"
    #rows = int(input("Number of rows"))
    with open(path,"r",newline='',encoding="utf-8") as csvfile:
        papers = csv.reader(csvfile,dialect="excel")
        for row in papers:
            print(row)
class paper:
    def __init__(self,doi,title,descr,authors,tags):
        self.doi = doi
        self.title = title
        self.descr = descr
        self.authors = authors
        self.tags = tags
    
    def setAutors(self,authors):  #TODO: implementar formateo correcot #nombre_apellido" ", 
         authors = name_surname
    
main()