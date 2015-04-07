import test
import selection_sort as selection_sort
import sorted_checker


def run_tests():
    print("\nSelection Sort tests")
    # setup
    numbers = [4, 1, 6, 2, 7, 9, 4, 3]
    sorted_numbers = [1, 2, 3, 4, 4, 6, 7, 9]

    # multiple_iterations
    test.are_equal("one iteration",
                   selection_sort.multiple_iterations(numbers, 1),
                   [1, 4, 6, 2, 7, 9, 4, 3])
    test.are_equal("two iterations",
                   selection_sort.multiple_iterations(numbers, 2),
                   [1, 2, 6, 4, 7, 9, 4, 3])
    test.are_equal("three iterations",
                   selection_sort.multiple_iterations(numbers, 3),
                   [1, 2, 3, 4, 7, 9, 4, 6])
    test.are_equal("four iterations",
                   selection_sort.multiple_iterations(numbers, 4),
                   [1, 2, 3, 4, 7, 9, 4, 6])
    test.are_equal("five iterations",
                   selection_sort.multiple_iterations(numbers, 5),
                   [1, 2, 3, 4, 4, 9, 7, 6])
    test.are_equal("six iterations",
                   selection_sort.multiple_iterations(numbers, 6),
                   sorted_numbers)

    # selection_sort
    test.are_equal("selection sort",
                   selection_sort.sort(numbers),
                   sorted_numbers)


if __name__ == "__main__":
    run_tests()
