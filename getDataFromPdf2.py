# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:23:24 2024

@author: asus
"""

import fitz
import json


def getDataFromPdf(path_to_pdf):


    pdf = fitz.open(path_to_pdf)
    content = pdf.get_toc()  # Extract table of contents
    
    data = {}  # Main dictionary to store the structure
    chapter_counter = 0
    section_counter = 0

    for i in content:
        level, name, page = i

        if level == 1:  # Top level (Chapter)
            chapter_counter += 1
            section_counter = 0
            data[str(chapter_counter)] = {
                "title": name,
                "sections": {}
            }
        elif level == 2:  # Second level (Section)
            section_counter += 1
            data[str(chapter_counter)]["sections"][str(section_counter)] = {
                "title": name,
                "subsections": {}
            }
        elif level == 3:  # Third level (Subsection)
            section_key = str(section_counter)
            if section_key in data[str(chapter_counter)]["sections"]:
                data[str(chapter_counter)]["sections"][section_key]["subsections"][name] = {
                    "title": name,
                    "page": page
                }

    return data


def writeToJson(struct, json_file):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(struct, f, ensure_ascii=False, indent=4)


# Example
file_pdf = "file.pdf"
json_file = "structure.json"


