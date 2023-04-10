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
    start_edge: str = data[0][0]
    final_edge: str = data[0][1]
    all_edges: str = data[1]

    ## Формирование словаря смежности взвешенного графа
    data = data[2:]
    for el in data:
        merge_list.append(tuple(el.split(', ')))

    ## Формирования словаря весов графа
    weight: dict = {el[0] + el[1]: el[2] for el in merge_list}

    for el in merge_list:

        if el[0] not in merge_dict:
            merge_dict[el[0]] = el[1]
        else:
            merge_dict[el[0]] += ',' + el[1]

        if el[1] not in merge_dict:
            merge_dict[el[1]] = el[0]
        else:
            merge_dict[el[1]] += ',' + el[0]

    for el in merge_dict:
        list_ = merge_dict[el].split(',')
        merge_dict[el] = list_

    return start_edge, final_edge, all_edges, merge_dict, weight


def bfs(graph, start, w):
    visited = [start]  # список посещенных вершин
    stack = [start]  # стек для обхода графа в ширину
    way = {}
    way_count = 0
    print(w)
    while stack:
        vertex = stack.pop(0)
        print(vertex)
        for neighbour in graph[vertex]:

            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
                key_merg = neighbour + vertex
            else:
                way_count = 0
            if key_merg in w:
                way_count += int(w[key_merg])
            else:
                way_count += int(w[key_merg[::-1]])

            way[key_merg] = way_count
    print(way)

    return visited


if __name__ == '__main__':
    start_edge, final_edge, all_edges, graph_merge_dict, weight = parse('test.txt')

    print('Result', bfs(graph_merge_dict, start_edge, weight))
