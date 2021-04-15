import itertools
from copy import deepcopy


def solution(times, times_limit):
    distance_matrix = deepcopy(times)
    neg_cycle = False
    for distance_list in distance_matrix:
        neg_cycle = relax_edges(distance_list, times)
        if neg_cycle: break

    base = []
    for i in range(len(distance_matrix) - 2):  # excluding first and last, since they need to be visited
        base.append(i + 1)

    path_generators = []
    for i in range(len(distance_matrix) - 2):
        path_generators.append(itertools.permutations(base, i + 1))

    best_path_max_bunnies = []

    if neg_cycle:
        best_path_max_bunnies = path_generators[-1].next()
    else:
        for path_generator in path_generators:
            best_path = []
            best_path_cost = times_limit + 1
            for path in path_generator:
                path_cost = calculate_path_cost(distance_matrix, path)
                if path_cost < best_path_cost:
                    best_path = path
                    best_path_cost = path_cost
            if not best_path:
                break
            best_path_max_bunnies = best_path

    best_path_max_bunnies = list(best_path_max_bunnies)
    for bunny in range(len(best_path_max_bunnies)):
        best_path_max_bunnies[bunny] -= 1
    list.sort(best_path_max_bunnies)
    return best_path_max_bunnies


def relax_edges(distance_list, times):
    for i in range(len(times) - 1):
        for starting_point in range(len(distance_list)):
            for destination in range(len(distance_list)):
                if starting_point == destination:
                    continue
                if distance_list[destination] > distance_list[starting_point] + times[starting_point][destination]:
                    distance_list[destination] = distance_list[starting_point] + times[starting_point][destination]

    # check for negative cycle
    dl_final = deepcopy(distance_list)
    for starting_point in range(len(distance_list)):
        for destination in range(len(distance_list)):
            if starting_point == destination:
                continue
            if distance_list[destination] > distance_list[starting_point] + times[starting_point][destination]:
                distance_list[destination] = distance_list[starting_point] + times[starting_point][destination]

    if 0 == cmp(dl_final, distance_list):
        return False
    else:
        return True


def calculate_path_cost(distance_matrix, path):
    curr = 0
    cost = 0
    for i in range(len(path)):
        next = path[i]
        cost += distance_matrix[curr][next]
        curr = path[i]
    cost += distance_matrix[curr][-1]  # last node
    return cost
