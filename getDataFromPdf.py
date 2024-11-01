import fitz
import json
import re

def getDataFromPdf(path_to_pdf):
    pdf = fitz.open(path_to_pdf)
    content = pdf.get_toc()
    
    data = {}
    chapter_counter = 0
    section_counter = 0

    for i in content:
        level, name, page_number = i  
        text = pdf[page_number - 1].get_text()  # Extract text from the page of each TOC entry

        if level == 1:
            chapter_counter += 1
            section_counter = 0
            data[str(chapter_counter)] = {
                "title": name,
                "sections": {},
                "text": text.strip(),  # Main chapter content
                "length": len(text)
            }
        
        elif level == 2:
            section_counter += 1
            section_number = f"{chapter_counter}.{section_counter}"
            section_text = pdf[page_number - 1].get_text()  # Extract section text
            data[str(chapter_counter)]["sections"][section_number] = {
                "title": re.sub(r'^\d+\.\s*', '', name),
                "subsections": {},
                "text": section_text.strip(),
                "length": len(section_text)
            }
        
        elif level == 3:
            subsection_counter = len(data[str(chapter_counter)]["sections"][section_number]["subsections"]) + 1
            subsection_number = f"{section_number}.{subsection_counter}"
            subsection_text = pdf[page_number - 1].get_text()  # Extract subsection text
            data[str(chapter_counter)]["sections"][section_number]["subsections"][subsection_number] = {
                "title": re.sub(r'^\d+\.\s*', '', name),
                "text": subsection_text.strip(),
                "length": len(subsection_text)
            }

    return data

def writeToJson(struct, json_file):
    with open(json_file, 'w') as f:
        json.dump(struct, f, ensure_ascii=False, indent=4)

file_pdf = "file.pdf"
json_file = "structure1.json"

structure = getDataFromPdf(file_pdf)
writeToJson(structure, json_file)
