import csv
from paper import paper

def main():
    path = input()
    csv2paper(path)

def csv2paper(path):
    '''Gets a csv file with papers that 
    has the same order of col that the class Paper
    and prints the markdown file in a folder'''   
    with open(path, "r", newline='', encoding="utf-8") as csvfile:
        papers = csv.reader(csvfile, dialect="excel")
        for row in papers:
            for col in row:
                col = col.strip()
            newPaper = paper(row[0],row[1],row[2],row[3],row[4])
            paper.writeFile(newPaper)
main()