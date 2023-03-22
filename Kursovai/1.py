


"""

            - Обход в глубину и ширину

            - Подсчет связанности графов

            - Выделение компонетиов связанности

            - Посмотреть словари

"""




# typle_test = [(a, b), (b, c), (c, d), (d,a)]
edges = []
vertex = []

with open('test_components.txt', 'r')  as file:
    text = file.readlines()

for el in text:
    vertex_a = el[0]
    vertex_b = el[1]
    vertex.append(vertex_a)
    vertex.append(vertex_b)
    edges.append((vertex_a, vertex_b))
dots = set(vertex)
print(f'Длина: {len(set(vertex))} \nТочки: {dots}')
print(f'Связи: {edges}')
# pos_a = []
# pos_b = []
# pos_c = []
# pos_d = []
# pos_f = []
def recur(dot_loc):
    if dot_loc not in set_1:
        set_1.add(dot_loc)
        p = 0


        for i in range(len(edges)):
            if dot_loc in edges[i]:
                p += 1
                vertex_1 = edges[i][0]
                vertex_2 = edges[i][1]
                if vertex_1 == dot_loc:
                    recur(vertex_2)
                elif vertex_2 == dot_loc:
                    recur(vertex_1)

        # print(p)

if __name__ == "__main__":
    set_1 = set()
    for dot in dots:
        recur(dot)
        print(f'Посещённые точки {set_1}')