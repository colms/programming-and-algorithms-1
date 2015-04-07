# bubble sort
import sorted_checker


def single_iteration(numbers):
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
    numbers_copy = numbers_original[:]

    # used to prevent infinite loop when is_sorted isn't implemented
    if sorted_checker.is_sorted(numbers_copy) is None:
        return None

    while not sorted_checker.is_sorted(numbers_copy):
        single_iteration(numbers_copy)
    return numbers_copy

""" output should look like this:
[4, 1, 6, 2, 7, 9, 4, 3]
> [1, 4, 6, 2, 7, 9, 4, 3]
> [1, 4, 2, 6, 7, 9, 4, 3]
> [1, 4, 2, 6, 7, 4, 9, 3]
> [1, 4, 2, 6, 7, 4, 3, 9]
[1, 4, 2, 6, 7, 4, 3, 9]
> [1, 2, 4, 6, 7, 4, 3, 9]
> [1, 2, 4, 6, 4, 7, 3, 9]
> [1, 2, 4, 6, 4, 3, 7, 9]
[1, 2, 4, 6, 4, 3, 7, 9]
> [1, 2, 4, 4, 6, 3, 7, 9]
> [1, 2, 4, 4, 3, 6, 7, 9]
[1, 2, 4, 4, 3, 6, 7, 9]
> [1, 2, 4, 3, 4, 6, 7, 9]
[1, 2, 4, 3, 4, 6, 7, 9]
> [1, 2, 3, 4, 4, 6, 7, 9]

> indicates mutation takes place within a single iteration
5 iterations in total
"""
