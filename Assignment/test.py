def are_equal(name, first, second):
    """Tests if two inputs are equal. Requires test name, first value to compare,
    and second value to compare.
    e.g. are_equal('To integer from string', int('5'), 5)
    """
    if first == second:
        print("Pass:", name)
        return True
    else:
        print("Fail:", name, ":: Expected:", second, ":: Received:", first)
        return False
