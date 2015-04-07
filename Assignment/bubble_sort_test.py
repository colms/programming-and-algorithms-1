import test
import bubble_sort as bubble_sort
import sorted_checker


def run_tests():
    print("\nBubble Sort tests")
    # setup
    numbers = [4, 1, 6, 2, 7, 9, 4, 3]
    sorted_numbers = [1, 2, 3, 4, 4, 6, 7, 9]

    # multiple_iterations
    test.are_equal("one iteration",
                   bubble_sort.multiple_iterations(numbers, 1),
                   [1, 4, 2, 6, 7, 4, 3, 9])
    test.are_equal("two iterations",
                   bubble_sort.multiple_iterations(numbers, 2),
                   [1, 2, 4, 6, 4, 3, 7, 9])
    test.are_equal("three iterations",
                   bubble_sort.multiple_iterations(numbers, 3),
                   [1, 2, 4, 4, 3, 6, 7, 9])
    test.are_equal("four iterations",
                   bubble_sort.multiple_iterations(numbers, 4),
                   [1, 2, 4, 3, 4, 6, 7, 9])
    test.are_equal("five iterations",
                   bubble_sort.multiple_iterations(numbers, 5),
                   sorted_numbers)

    # bubble_sort
    test.are_equal("bubble sort",
                   bubble_sort.sort(numbers),
                   sorted_numbers)


if __name__ == "__main__":
    run_tests()
