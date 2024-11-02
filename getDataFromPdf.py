import fitz
import json
import re

def extract_text(page, keywords):
    """Extracts text and validates it based on keywords related to title."""
    text = page.get_text().strip()
    
    # Check if any keyword from the title is in the text; if not, text may be unrelated
    if not any(keyword.lower() in text.lower() for keyword in keywords):
        # Try limiting to first paragraph if unrelated text is found
        paragraphs = text.split("\n\n")
        for paragraph in paragraphs:
            if any(keyword.lower() in paragraph.lower() for keyword in keywords):
                return paragraph.strip()  # Return only relevant paragraph
        return None  # Return None if no relevant paragraph is found
    return text

def getDataFromPdf(path_to_pdf):
    pdf = fitz.open(path_to_pdf)
    content = pdf.get_toc()
    
    data = {}  # Main dictionary to store structure
    chapter_counter = 0
    section_counter = 0

    for i in content:
        try:
            level, name, page_number = i
            if page_number < 1 or page_number > pdf.page_count:
                continue  # Skip if page number is out of bounds

            # Get keywords from title for validation
            keywords = re.split(r'[\s,]', re.sub(r'^\d+\.\s*', '', name))
            page = pdf[page_number - 1]
            text = extract_text(page, keywords)
            
            if text is None:
                continue  # Skip this section if no relevant text found

            if level == 1:
                chapter_counter += 1
                section_counter = 0
                data[str(chapter_counter)] = {
                    "title": name,
                    "sections": {},
                    "text": text,
                    "length": len(text)
                }
            
            elif level == 2:
                section_counter += 1
                section_number = f"{chapter_counter}.{section_counter}"
                data[str(chapter_counter)]["sections"][section_number] = {
                    "title": re.sub(r'^\d+\.\s*', '', name),
                    "subsections": {},
                    "text": text,
                    "length": len(text)
                }
            
            elif level == 3:
                section_number = f"{chapter_counter}.{section_counter}"
                if section_number in data[str(chapter_counter)]["sections"]:
                    subsection_counter = len(data[str(chapter_counter)]["sections"][section_number]["subsections"]) + 1
                    subsection_number = f"{section_number}.{subsection_counter}"
                    data[str(chapter_counter)]["sections"][section_number]["subsections"][subsection_number] = {
                        "title": re.sub(r'^\d+\.\s*', '', name),
                        "text": text,
                        "length": len(text)
                    }
        except Exception as e:
            print(f"Error processing TOC entry {i}: {e}")
            continue

    return data

def writeToJson(struct, json_file):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(struct, f, ensure_ascii=False, indent=4)

file_pdf = "file.pdf"
json_file = "structure.json"

structure = getDataFromPdf(file_pdf)
writeToJson(structure, json_file)
