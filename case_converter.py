# # Bismillah
# """
# Created on Sat Sep 28 20:09:08 2024

# @author: Faxriddin
# """

# def convert_to_snake_case(pascal_or_camel_cased_string):
#     # snake_cased_char_list = []
#     # for char in pascal_or_camel_cased_string:
#     #     if char.isupper():
#     #         converted_character = '_' + char.lower()
#     #         snake_cased_char_list.append(converted_character)
#     #     else:
#     #         snake_cased_char_list.append(char)
#     # snake_cased_string = ''.join(snake_cased_char_list)
#     # clean_snake_cased_string = snake_cased_string.strip('_')

#     # return clean_snake_cased_string

#     snake_cased_char_list = [
#         '_' + char.lower() if char.isupper()
#         else char
#         for char in pascal_or_camel_cased_string
#     ]

#     return ''.join(snake_cased_char_list).strip('_')

# def main():
#     print(convert_to_snake_case('IAmAPascalCasedString'))

# main()

def main(a):

    # Сортируем массив
    a.sort()
    
    # Выводим второй элемент (с индексом 1)
    print(a[1])

if __name__ == '__main__':
    a = [1000,-1000,0]
    main(a)
