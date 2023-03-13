
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
'''


def to_camel_case(text):
    if text:
        text_result = text[0]
        tire_point = 0

        for i in range(len(text)):

            if text[i] == '-' or text[i] == '_':
                tire_point = i + 1
                text_result += text[i + 1].upper()

            elif i != tire_point:
                text_result += text[i]
                print(text_result)

        return text_result
    return text
