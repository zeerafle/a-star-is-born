"""
Modul untuk menghitung solusi jalur labirin terbaik menggunakan
metode pencarian heuristik A * Search
"""

import sys

from  maze5  import generate_graph as maze5
from  maze8  import generate_graph as maze8
from  maze10 import generate_graph as maze10
from  maze12 import generate_graph as maze12

MAX_POSSIBLE_VALUE = sys.maxsize

def astar_search(graph, start, goal):
    path = []
    explored_nodes = list()
    if start == goal:
        return path, explored_nodes

    path.append(start)
    path_cost = get_manhattan_heuristic(start, goal)

    frontier = [(path_cost, path)]
    while len(frontier) > 0:
        path_cost_till_now, path_till_now = pop_frontier(frontier)
        current_node = path_till_now[-1]
        path_cost_till_now = path_cost_till_now - get_manhattan_heuristic(current_node, goal)
        explored_nodes.append(current_node)
        if current_node == goal:
            return path_till_now, explored_nodes

        neighbours = graph[current_node]

        neighbours_list_int = [int(n) for n in neighbours]
        neighbours_list_int.sort(reverse=False)
        neighbours_list_str = [str(n) for n in neighbours_list_int]

        for neighbour in neighbours_list_str:
            path_to_neighbour = path_till_now.copy()
            path_to_neighbour.append(neighbour)
            extra_cost = 1
            neighbour_cost = (extra_cost
                              + path_cost_till_now
                              + get_manhattan_heuristic(neighbour, goal))
            new_element = (neighbour_cost, path_to_neighbour)

            is_there, indexx, neighbour_old_cost, _ = get_frontier_params_new(neighbour, frontier)

            if (neighbour not in explored_nodes) and not is_there:
                frontier.append(new_element)

            elif is_there:
                if neighbour_old_cost > neighbour_cost:
                    frontier.pop(indexx)
                    frontier.append(new_element)

    return None, None

def pop_frontier(frontier):
    if len(frontier) == 0:
        return None

    min_value = MAX_POSSIBLE_VALUE
    max_values = []
    for key, path in frontier:
        if key == min_value:
            max_values.append(path)
        elif key < min_value:
            min_value = key
            max_values.clear()
            max_values.append(path)

    max_values = sorted(max_values, key=lambda x: x[-1])
    desired_value = max_values[0]
    frontier.remove((min_value, max_values[0]))
    return min_value, desired_value

def get_frontier_params_new(node, frontier):
    for i in range(len(frontier)):
        curr_tuple = frontier[i]
        cost, path = curr_tuple
        if path[-1] == node:
            return True, i, cost, path
    return False, None, None, None

def get_manhattan_heuristic(node, goal):
    i, j = divmod(int(node), 8)
    i_goal, j_goal = divmod(int(goal), 8)
    i_delta = abs(i - i_goal)
    j_delta = abs(j - j_goal)
    manhattan_dist = i_delta + j_delta
    return manhattan_dist

if __name__ == '__main__':
    graph_neighbours5 = maze5()
    graph_neighbours8 = maze8()
    graph_neighbours10 = maze10()
    graph_neighbours12 = maze12()

    print("============ AStar Search ================")
    path_astar, explored_astar = astar_search(graph_neighbours10, '1', '50')
    print("Jalur:", path_astar)
    print("Tereksplor: ", explored_astar)
    print(len(explored_astar))
    print()
