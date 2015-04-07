import test
import sorted_checker as sorted_checker


def run_tests():
    print("\nSorted Checker tests")

    # setup
    numbers = [4, 1, 6, 2, 7, 9, 4, 3]
    sorted_numbers = [1, 2, 3, 4, 4, 6, 7, 9]

    # is_sorted
    test.are_equal("full list unsorted",
                   sorted_checker.is_sorted(numbers), False)
    test.are_equal("full list sorted",
                   sorted_checker.is_sorted(sorted_numbers), True)
    test.are_equal("one element list sorted",
                   sorted_checker.is_sorted([3]), True)
    test.are_equal("empty list sorted",
                   sorted_checker.is_sorted([]), True)


if __name__ == "__main__":
    run_tests()
