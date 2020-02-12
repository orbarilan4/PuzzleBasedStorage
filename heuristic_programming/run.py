from heuristic_programming.state import State
from heuristic_programming.heuristics.heuristic import Heuristic
from heuristic_programming.heuristics.manhattan_distance import manhattan_distance
from heuristic_programming.heuristics.manhattan_distance_plus_blocks import manhattan_distance_plus_blocks
from heuristic_programming.heuristics.zero_dummy import zero_dummy
from heuristic_programming.a_star import a_star
from heuristic_programming.grid.grid_summary import get_grid_summary
import time
from settings import *
from heuristic_programming.states.generate_states import generate_state
import random
import os
import shutil


def main():
    iterations_number = int(ITERATIONS_NUMBER)
    create_new_results_directory("results")
    for i in range(1, 6):
        print("\n\nRESULTS FOR " + str(i) + " ESCORTS")
        start_states = generate_state(iterations_number, 5, {ESCORT: i, LOAD: 1, PACKAGE: 24-i}, [[random.randint(0, 4), random.randint(0, 4)]])
        f = open("results\_for_" + str(i) + "_escorts.txt", "a")

        f.write("\nFor A* Algorithm: (with manhattan distance considering blocks heuristic)")
        f.write("\n================================================================================")
        start_time = time.time()
        sum_of_developed_states = 0
        sum_of_close_lists = 0
        sum_of__path_lengths = 0
        for start_state in start_states:
            #print(start_state.grid)
            #print(start_state.extraction_points)
            path, number_of_developed_states, close_list_size = \
                a_star(start_state, Heuristic(manhattan_distance_plus_blocks))
            sum_of__path_lengths += len(path)
            sum_of_developed_states += number_of_developed_states
            sum_of_close_lists += close_list_size
        f.write("\nthe sum of the path lengths for all iterations: " + str(sum_of__path_lengths))
        f.write("\nthe avg of developed states ever in open-list: " + str(sum_of_developed_states / iterations_number))
        f.write("\nthe avg of the close-list size: " + str(sum_of_close_lists / iterations_number))
        f.write("\nthe avg CPU time is: " + str((time.time() - start_time) / iterations_number))

        f.write("\n\nFor A* Algorithm: (with manhattan distance heuristic)")
        f.write("\n================================================================================")
        start_time = time.time()
        sum_of_developed_states = 0
        sum_of_close_lists = 0
        sum_of__path_lengths = 0
        for start_state in start_states:
            #print(start_state.grid)
            #print(start_state.extraction_points)
            path, number_of_developed_states, close_list_size =\
                a_star(start_state, Heuristic(manhattan_distance))
            sum_of__path_lengths += len(path)
            sum_of_developed_states += number_of_developed_states
            sum_of_close_lists += close_list_size
        f.write("\nthe sum of the path lengths for all iterations: " + str(sum_of__path_lengths))
        f.write("\nthe avg of developed states ever in open-list: " + str(sum_of_developed_states / iterations_number))
        f.write("\nthe avg of the close-list size: " + str(sum_of_close_lists / iterations_number))
        f.write("\nthe avg CPU time is: " + str((time.time() - start_time) / iterations_number))
    #
    # print("\nBFS Algorithm: (A* with zero dummy heuristic)")
    # print("================================================================================")
    # start_time = time.time()
    # sum_of_developed_states = 0
    # sum_of_close_lists = 0
    # sum_of__path_lengths = 0
    # for start_state in start_states:
    #     # print(start_state.grid)
    #     path, number_of_developed_states, close_list_size =\
    #         a_star(start_state, create_all_final_states(start_state), Heuristic(zero_dummy))
    #     sum_of__path_lengths += len(path)
    #     sum_of_developed_states += number_of_developed_states
    #     sum_of_close_lists += close_list_size
    # print("the sum of the path lengths for all iterations: " + str(sum_of__path_lengths))
    # print("the avg of developed states ever in open-list: " + str(sum_of_developed_states / iterations_number))
    # print("the avg of the close-list size: " + str(sum_of_close_lists / iterations_number))
    # print("the avg CPU time is: " + str((time.time() - start_time) / iterations_number))

        f.close()


def create_new_results_directory(name):
    if os.path.exists(name):
        shutil.rmtree(name)
    os.makedirs(name)


if __name__ == '__main__':
    main()
