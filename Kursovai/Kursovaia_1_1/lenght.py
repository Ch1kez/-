

def parse(file_name):
    data = []
    merge_list = []
    merge_dict = {}

    # Считывание данных из файла
    with open(file_name, 'r', encoding='utf-8') as file:
        info = file.read()

    # Отделение подписей и данных
    for el in info.split('\n'):
        if '#' not in el:
            data.append(el)

    # Формирование итоговых данных
    start_edge = data[0][0]
    final_edge = data[0][1]
    all_edges = data[1]

    # Формирование списка смежности взвешенного графа
    data = data[2:]
    for el in data:
        merge_list.append(tuple(el.split(', ')))

    print(merge_list)

    merge_lists = []

    for el in merge_list:
        if  el[0] not in merge_dict:
            merge_dict[el[0]] = el[1]
        else:
            merge_dict[el[0]] += ',' + el[1]

        if  el[1] not in merge_dict:
            merge_dict[el[1]] = el[0]
        else:
            merge_dict[el[1]] += ',' + el[0]

    print(merge_dict)
    for el in merge_dict:
        merge_lists.append(merge_dict[el].split(','))
    print(merge_lists)

    return start_edge, final_edge, all_edges, merge_list

def bfs():

    start_edge, final_edge, all_edges, merge_list = parse('test')
    visited = []  # список посещенных вершин
    stack = []  # стек для обхода графа в ширину
    stack.append(merge_list[0])  # добавляем в стек стартовую вершину

    while stack:
        vertex = stack.pop(0)
        print(vertex)
        if vertex not in visited:
            print(vertex[0])
            visited.append(vertex[0][0][0])
            stack.extend([x for x in merge_list[vertex] if x not in visited])

    return visited



if __name__ == '__main__':
    print('Result', bfs())