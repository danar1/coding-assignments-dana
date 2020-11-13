def is_won_loto(list_of_tuples, loto_number):
    """
    This function get list of tuples and a loto number
    Return True if:
    - The max number in ALL tuples is equal to the given loto_number, Or
    - The sum of the first 2 numbers in ALL the tuples is equal to the given loto_number, Or
    - The next to last number in ALL the tuples is equal to the given loto_number, Or
    Otherwise return False
    * notes -
      Using builtins (avoid explicit usage of 'for' loop)
      Assuming len(list_of_tuples) >= 2
    """
    is_max_equal_loto_num = all(map(lambda _tuple: max(_tuple) == loto_number, list_of_tuples))
    is_sum_first_two_equal_loto_num = all(map(lambda _tuple: sum(_tuple[:2]) == loto_number, list_of_tuples))
    is_next_last_num_equal_loto_num = all(map(lambda _tuple: _tuple[-2] == loto_number, list_of_tuples))
    if is_max_equal_loto_num or is_sum_first_two_equal_loto_num or is_next_last_num_equal_loto_num:
        return True
    return False


if __name__ == '__main__':
    has_max_of_8 = [(1, 5, 4, 8, 0, 2, 3), (2, 6, 2, 8, 8), (3, 8, 0, 4, 7)]
    print("tuple of {} with loto number of {} should return `True`. Result: ".format(has_max_of_8, 8),
          is_won_loto(has_max_of_8, 8))

    first_two_numbers_sum_is_8 = [(3, 5, 4), (2, 6, 2, 3, 5), (4, 4, 9, 4, 7)]
    print("tuple of {} with loto number of {} should return `True`. Result: ".format(first_two_numbers_sum_is_8, 8),
          is_won_loto(first_two_numbers_sum_is_8, 8))

    next_to_last_number_is_always_8 = [(3, 8, 4), (2, 6, 2, 8, 5), (8, 4)]
    print("tuple of {} with loto number of {} should return `True`. Result: ".format(next_to_last_number_is_always_8, 8),
          is_won_loto(next_to_last_number_is_always_8, 8))

    only_one_of_the_tuples_have_max_of_8 = [(3, 5, 4), (2, 8, 2, 3, 5), (4, 9, 8)]
    print("tuple of {} with loto number of {} should return `False`. Result: ".format(only_one_of_the_tuples_have_max_of_8, 8),
          is_won_loto(only_one_of_the_tuples_have_max_of_8, 8))

    nothing_is_true_in_this_list = [(3, 3, 9), (8, 6, 2), (4, 1, 9, 8)]
    print("tuple of {} with loto number of {} should return `False`. Result: ".format(nothing_is_true_in_this_list, 8),
          is_won_loto(nothing_is_true_in_this_list, 8))

