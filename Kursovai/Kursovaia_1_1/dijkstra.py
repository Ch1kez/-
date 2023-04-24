from parse_txt import parse
from heapq import *


# Реализация алгоритма Дейкстры (на куче)
def dijkstra(start_node, finish_node, graph_node):
    queue = []
    heappush(queue, (0, start_node))
    cost_visited = {start_node: 0}
    visited = {start_node: None}

    while queue:
        cur_cost, node = heappop(queue)
        if node == finish_node:
            break

        next_nodes = graph_node[node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = node

    return visited, cost_visited


if __name__ == '__main__':

    start = parse('test')[0]
    finish = parse('test')[1]
    graph = parse('test')[2]

    path = f'{finish}'
    visited_nodes, cost_visited_nodes = dijkstra(start, finish, graph)
    cur_node = finish

    print(f'\nКратчайший маршрут от {start} до {finish}:')

    while cur_node != start:
        cur_node = visited_nodes[cur_node]
        path += f' >--- {cur_node} '
    path = path[::-1]
    print(path)
    print(f'Длина кратчайшего маршрута от {start} до {finish}: {cost_visited_nodes[finish]}')
