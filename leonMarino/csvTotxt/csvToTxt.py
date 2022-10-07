import csv
import re



def main():
    print("Bienvenido al conversor")
    #path = str(input("File path for reading, remember to have the right formating \n:"))
    #path = path[1:len(path)-1]
    path = "D:\Drive\Analisis Trabajos - Copy.csv"
    csv2paper(path)

#TODO: check excel for title with error and fix regex 
def clean_text(text):
    text = text.lower()
    text = re.sub("[\\()/]","",text)
    text = re.sub("[,.:;-]","",text)
    #text = re.sub("\\d","",text)
    text = str(text).strip()
    return text
    
    #TODO: separa logica
def csv2paper(path):
    '''Gets a csv file with papers with that 
    has the same order of col that the class Paper'''   
    with open(path, "r", newline='', encoding="utf-8") as csvfile:
        papers = csv.reader(csvfile, dialect="excel")
        for row in papers:
            for col in row:
                col = col.strip()
            newPaper = paper()
            paper.createPaper(newPaper,row[1],row[2],row[0],row[3],row[6])
            paper.writeFile(newPaper)

def str2list(text):
    return str.split(text,",")

def prepareText(text):
    text = re.sub(";","_",text)
    text = re.sub("[ .]","",text)
    return text

class paper:
    def __init__(self):
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
        self.paper = dict()
        #self.title = title,

    def setTitle(self, title):
        self.paper["title"] = (title)
        
    def setAuthors(self, author):
        """List of Authors"""
        author = prepareText(author)
        self.paper["author"] = (str2list(author))

    def setDoi(self, doi):
        self.paper["doi"] = (doi)

    def setDescr(self, description):
        self.paper["description"] = (description)

    def setTags(self, tags):
        """List of tags"""
        tags = prepareText(tags)
        self.paper["tags"] = (str2list(tags))

    def createPaper(self,title, author, doi, description, tags):
        self.setTitle(title)
        self.setAuthors(author)
        self.setDoi(doi)
        self.setDescr(description)
        self.setTags(tags)

    def paper2string(self):
        """Transform the object to string"""
        paper = self.paper
        file = ""
        file += f"# {paper['title']}\n"                     # Titulo
        file += f"## Authors\n"                             ## Autores
        for author in paper["author"]:        
            file += f"#{author}"                            #Nombre_Apellido
        file += f"\n## DOI\n {paper['doi']}\n"              ## DOI + link
        file += f"## Description\n{paper['description']}\n" ## Descripción abstract
        file += f"## Tags\\\Key words\n"
        for tag in paper["tags"]:        
            file += f"#{tag}"                                                 
        return file

    def writeFile(self):
        """Writes the obj as a string"""
        txtTitle = self.paper["title"]
        txtTitle = clean_text(txtTitle)
        with open(f"{txtTitle}.txt" , "w",encoding="utf-8") as f:
            f.write(self.paper2string())

main()