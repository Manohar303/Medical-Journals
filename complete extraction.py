from tika import parser
import spacy
from scispacy.abbreviation import AbbreviationDetector
import re 

nlp = spacy.load("en_core_sci_sm")


Pdf=parser.from_file("G:\\Srivatsa@study\\Data Science\\Project\\project-1\\data\\27-30.pdf")
pDf=parser.from_file("G:\\Srivatsa@study\\Data Science\\Project\\project-1\\data\\888-97.pdf")
pdF=parser.from_file("G:\\Srivatsa@study\\Data Science\\Project\\project-1\\data\\888-896.pdf")
PDF=parser.from_file("G:\\Srivatsa@study\\Data Science\\Project\\project-1\\data\\603913.pdf")

data1=Pdf['content']
data2=pDf['content']
data3=pdF['content']
data4=PDF['content']

data1=data1.strip()
data2=data2.strip()
data3=data3.strip()
data4=data4.strip()

# Add the abbreviation pipe to the spacy pipeline.
nlp.add_pipe("abbreviation_detector")

doc1 = nlp(data1)
doc2 = nlp(data2)
doc3 = nlp(data3)
doc4 = nlp(data4)


print("Abbreviation", "\t", "Definition")
extract1,extract2,extract3,extract4=[],[],[],[]
for abrv in doc1._.abbreviations:
	extract1.append(f"{abrv} \t ({abrv.start}, {abrv.end}) {abrv._.long_form}")
for abrv in doc2._.abbreviations:
	extract2.append(f"{abrv} \t ({abrv.start}, {abrv.end}) {abrv._.long_form}")
for abrv in doc3._.abbreviations:
	extract3.append(f"{abrv} \t ({abrv.start}, {abrv.end}) {abrv._.long_form}")
for abrv in doc4._.abbreviations:
	extract4.append(f"{abrv} \t ({abrv.start}, {abrv.end}) {abrv._.long_form}")

   
extract=extract1+extract2+extract3+extract4
extract="\n".join(extract)
extract=extract.strip()    
with open("data.txt", "w",encoding='utf-8') as file:
    file.write(extract)
        import os
        os.getcwd()
        