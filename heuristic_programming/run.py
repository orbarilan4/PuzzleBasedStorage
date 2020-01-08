from heuristic_programming.state import State
from heuristic_programming.heuristics.heuristic import Heuristic
from heuristic_programming.heuristics.manhattan_distance import manhattan_distance
from heuristic_programming.heuristics.zero_dummy import zero_dummy
from heuristic_programming.states.final_states import create_all_final_states
from heuristic_programming.a_star import a_star
import random
from settings import *
import numpy as np


# Generate basic state
def generate_state(grid_rows_number, grid_cols_number, load_points, extraction_points):
    grid = np.full((grid_rows_number, grid_cols_number), LOAD)
    for i in range(grid_cols_number):
        for j in range(grid_cols_number):
            # If it is not a 'load point' it will be 'escort' or 'package'
            if [i, j] not in load_points:
                grid[i, j] = random.choice([ESCORT, PACKAGE])
    grid[1,0] = ESCORT
    return State(grid, extraction_points, None)


def main():
    start_states = []
    for i in range(5):
        start_states.append(generate_state(3, 3, [[0, 0]], [[2, 2]]))

    sum_of_developed_states = 0
    sum_of_close_lists = 0
    for start_state in start_states:
        print(start_state.grid)
        path, number_of_developed_states, close_list_size =\
            a_star(start_state, create_all_final_states(start_state), Heuristic(manhattan_distance))
        sum_of_developed_states += number_of_developed_states
        sum_of_close_lists += close_list_size
    print("the avg of developed states ever in open list: " + str(sum_of_developed_states / 5))
    print("the avg of close list: " + str(sum_of_close_lists / 5))

    sum_of_developed_states = 0
    sum_of_close_lists = 0
    for start_state in start_states:
        print(start_state.grid)
        path, number_of_developed_states, close_list_size =\
            a_star(start_state, create_all_final_states(start_state), Heuristic(zero_dummy))
        sum_of_developed_states += number_of_developed_states
        sum_of_close_lists += close_list_size
    print("the avg of developed states ever in open list: " + str(sum_of_developed_states / 5))
    print("the avg of close list: " + str(sum_of_close_lists / 5))


if __name__ == '__main__':
    main()