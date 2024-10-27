import fitz
import json

def extract_structure_from_pdf(pdf_path):
    # Открываем PDF-файл
    pdf_document = fitz.open(pdf_path)
    
    # Извлекаем оглавление (toc - table of contents)
    toc = pdf_document.get_toc()

    # Структура данных
    structure = {}

    # Итерация по оглавлению для формирования структуры
    for item in toc:
        level, title, page = item
        # Уровень 1 - глава, уровень 2 - раздел, уровень 3 - подраздел
        if level == 1:
            current_chapter = title
            structure[current_chapter] = {}
        elif level == 2:
            current_section = title
            structure[current_chapter][current_section] = {}
        elif level == 3:
            current_subsection = title
            structure[current_chapter][current_section][current_subsection] = page
    
    # Возвращаем итоговую структуру данных
    return structure

def save_structure_as_json(structure, json_path):
    # Сохранение структуры в формате JSON
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(structure, json_file, ensure_ascii=False, indent=4)

# Пример использования
pdf_path = "your_file.pdf"  # Укажите путь к вашему PDF файлу
json_path = "structure.json"  # Имя файла для сохранения структуры

structure = extract_structure_from_pdf(pdf_path)
save_structure_as_json(structure, json_path)
