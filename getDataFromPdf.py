# import fitz
# import json

# def getDataFromPdf(path_to_pdf):
#     pdf = fitz.open(path_to_pdf)
#     content = pdf.get_toc() # Служит для извлечения оглавлений
    
#     data = {} # Основной словарь
#     chapter_counter = 0
#     section_counter = 0

#     for i in content:
#         level, name, page = i
        
#         if level == 1:
#             chapter_counter += 1
#             section_counter = 0
#             data[str(chapter_counter)] = {
#                 "title": name,
#                 "sections": {}
#             }
        
#         elif level == 2:
#             section_counter += 1
#             data[str(chapter_counter)]["sections"][str(section_counter)] = {
#                 "title": name,
#                 "subsections": {}
#             }
        
#         elif level == 3:
#             data[str(chapter_counter)]["sections"][str(section_counter)]["subsections"][name] = {
#                 "title": name,
#                 "page": page
#             }
    
#     return data

# def writeToJson(struct, json_file):
#     f = open(json_file, 'w')
#     json.dump(struct, f, ensure_ascii=False, indent=4)
#     f.close()



# # Example
# file_pdf = "file.pdf"
# json_file = "structure.json"

# structure = getDataFromPdf(file_pdf)
# writeToJson(structure, json_file)

import fitz
import json

def getDataFromPdf(path_to_pdf):
    pdf = fitz.open(path_to_pdf)
    content = pdf.get_toc()
    
    data = {}
    chapter_counter = 0
    section_counter = 0

    for i in content:
        level, name, page = i
        
        if level == 1:
            chapter_counter += 1
            section_counter = 0
            data[str(chapter_counter)] = {
                "title": name,
                "sections": {}
            }
        
        elif level == 2:
            section_counter += 1
            section_number = f"{chapter_counter}.{section_counter}"
            data[str(chapter_counter)]["sections"][section_number] = {
                "title": name,
                "subsections": {}
            }
        
        elif level == 3:
            subsection_counter = len(data[str(chapter_counter)]["sections"][section_number]["subsections"]) + 1
            subsection_number = f"{section_number}.{subsection_counter}"
            data[str(chapter_counter)]["sections"][section_number]["subsections"][subsection_number] = {
                "title": name,
                "page": page
            }

    return data

def writeToJson(struct, json_file):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(struct, f, ensure_ascii=False, indent=4)

# Example usage
file_pdf = "file.pdf"
json_file = "structure1.json"

structure = getDataFromPdf(file_pdf)
writeToJson(structure, json_file)



