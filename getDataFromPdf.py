import fitz
import json


def getDataFromPdf(path_to_pdf):
    pdf = fitz.open(path_to_pdf)
    content = pdf.get_toc() # Служит для извлечения оглавлений
    data = {} # Основной словарь
    
    for i in content:
        if i[0] == 1:
            title = i[1]
            data[title] = {}
        if i[0] == 2:
            chapter = i[1]
            data[title][chapter] = {}
        if i[0] == 3:
            subsection = i[1]
            data[title][chapter][subsection] = i[2]
    return data

def writeToJson(struct, json_file):
    f = open(json_file, 'w')
    json.dump(struct, f, ensure_ascii=False, indent=4)
    f.close()


# Example
file_pdf = "file.pdf"
json_file = "structure.json"            

structure = getDataFromPdf(file_pdf)
writeToJson(structure, json_file)
    
    

