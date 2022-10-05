import csv
from ast import Num
from codecs import charmap_build

import numpy as np
import pandas as pd


def main():
    print("Bienvenido al conversor")
    #path = str(input("File path for reading, remember to have the right formating \n:"))
    #path = path[1:len(path)-1]
    path = "D:\Drive\Analisis Trabajos - Copy.csv"
    #rows = int(input("Number of rows"))

class paper:
    def __init__(self, title, paper):
        '''	# Titulo
            ## Autores
             #Nombre_Apellido
            ## DOI
             link
            ## Descripción abstract
             lipsum lipus 
            ## Tags/palabras claves
             #institucion, #revista, #tema, #lugar 
        '''
        paper = dir()
        self.paper = paper
        self.title = title,

    def setAuthors(self, author):
        """List of Authors"""
        self.paper["author"] = (author)

    def setDoi(self, doi):
        self.paper["doi"] = (doi)

    def setDescr(self, description):
        self.paper["description"] = (description)

    def setTags(self, tags):
        """List of tags"""
        self.paper["tags"] = (tags)

    def createPaper(self, author, doi, description, tags):
        self.paper["title"] = (self.title)
        self.paper.setAuthors(author)
        self.paper.setDoi(doi)
        self.paper.setDescr(description)
        self.paper.setTags(tags)

    def paper2string(self):
        """Transform the object to string"""
        paper = self.paper
        file = ""
        file += f"# {paper['title']}\n"                     # Titulo
        file += f"## Authors\n"                             ## Autores
        for authors in paper["authors"]:        
            for author in authors: 
                str(author).replace(" ","_")                #Nombre_Apellido
                file += f"#{author}"
        file += f"\n## DOI\n {paper['doi']}\n"              ## DOI + link
        file += f"## Description\n{paper['description']}\n" ## Descripción abstract
        file += f"## Tags\\\Key words\n"
        for tags in paper["tags"]:        
            for tag in tags: 
                str(tag).replace(" ","_")                   #tag
                file += f"#{tag}"                                                 
        return file

    def getString(self):
        """Writes the obj as a string"""
        with open(f"{self.title}.txt" , "w") as f:
            f.write(self.paper2string())

    def csv2paper(path):   
        with open(path, "r", newline='', encoding="utf-8") as csvfile:
            papers = csv.reader(csvfile, dialect="excel")
        for row in papers:
            print(row)        
main()
