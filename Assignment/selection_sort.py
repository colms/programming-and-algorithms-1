# selection sort
import sorted_checker


def single_iteration(numbers, iteration_number):
    """Performs one iteration of the sorting algorithm.
    Mutates input list and does not return a value.
    """
    pass


def multiple_iterations(numbers_original, num_iterations_to_complete):
    """Performs the specified number of iterations of the sorting algorithm.
    Returns a sorted copy of the list of numbers.
    """
    pass


def sort(numbers_original):
    """Sorts a list of numbers in ascending order using the bubble sort algorithm.
    Returns a sorted copy of the list of numbers.
    """
    i = 0
    numbers_copy = numbers_original[:]

    # used to prevent infinite loop when is_sorted isn't implemented
    if sorted_checker.is_sorted(numbers_copy) is None:
        return None

    while not sorted_checker.is_sorted(numbers_copy):
        single_iteration(numbers_copy, i)
        i += 1
    return numbers_copy

""" output should look like this:
[4, 1, 6, 2, 7, 9, 4, 3]
[1, 4, 6, 2, 7, 9, 4, 3]
[1, 2, 6, 4, 7, 9, 4, 3]
[1, 2, 3, 4, 7, 9, 4, 6]
[1, 2, 3, 4, 7, 9, 4, 6]
[1, 2, 3, 4, 4, 9, 7, 6]
[1, 2, 3, 4, 4, 6, 7, 9]
7 iterations in total
"""
