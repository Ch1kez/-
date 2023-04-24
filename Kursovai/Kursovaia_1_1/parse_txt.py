def parse(file_name):
    data = []
    merge_list = []

    # Считывание данных из файла
    with open(file_name, 'r', encoding='utf-8') as file:
        info = file.read()

    # Отделение подписей и данных
    for el in info.split('\n'):
        if '#' not in el:
            data.append(el)

    # Формирование итоговых данных
    start_edge: str = data[0][0]
    final_edge: str = data[0][3]
    all_edges: str = data[1]

    # Формиparseрование словаря смежности взвешенного графа
    data = data[2:]
    for el in data:
        merge_list.append(tuple(el.split(', ')))

    # Формирования словаря весов графа
    weight: dict = {el[0] + el[1]: el[2] for el in merge_list}

    # Формирования графа в виде словаря
    dict_ = {}
    for el in merge_list:
        # print(dict_)
        # for ell in el:
        if el[0] in dict_:
            dict_[el[0]].append(tuple([int(el[2]), el[1]]))
        elif el[0] not in dict_:
            dict_[el[0]] = [tuple([int(el[2]), el[1]])]

        if el[1] in dict_:
            dict_[el[1]].append(tuple([int(el[2]), el[0]]))
        elif el[1] not in dict_:
            dict_[el[1]] = [tuple([int(el[2]), el[0]])]

    return start_edge, final_edge, dict_


if __name__ == '__main__':
    print(f'Начальная точка графа (пути): {parse("test")[0]}')
    print(f'Конечная точка графа (пути): {parse("test")[1]}')
    print(f'Граф, представленный ввиде списков смежности (словарь):\n {parse("test")[2]}')

