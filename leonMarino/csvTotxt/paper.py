import re
import os
#functions aux
#TODO: check excel for title with error and fix regex 
def clean_text(text):
    text = text.lower()
    text = re.sub("[\\()/]","",text)
    text = re.sub("[,.:;-]","",text)
    #text = re.sub("\\d","",text)
    text = str(text).strip()
    return text

def str2list(text):
    return str.split(text,",")

def prepareText(text):
    text = re.sub(";","_",text)
    text = re.sub("[ .]","",text)
    return text

#writeFile aux, creates the dir
def createDir(name):
    if(not os.path.exists(name) and os.path.basename != name):
        os.mkdir(name)


class paper:
    def __init__(self,title, author, doi, description, tags):
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
        self.setTitle(title)
        self.setAuthors(author)
        self.setDoi(doi)
        self.setDescr(description)
        self.setTags(tags)
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
        if(os.path.basename(os.getcwd()) != "files"):
            createDir("files")
            os.chdir("files")
        with open(f"{txtTitle}.txt" , "w",encoding="utf-8") as f:
            f.write(self.paper2string())
    