#                  DO NOT EDIT!                       #
#  this is a test file that verifies the assignments  #
#    was submitted according to the requirements      #
from session1.src import assignment2


def test_tuple_has_max_of_8_will_return_true():
    has_max_of_8 = [(1, 5, 4, 8, 0, 2, 3), (2, 6, 2, 8, 8), (3, 8, 0, 4, 7)]
    assert assignment2.is_won_loto(has_max_of_8, 8), \
        "tuple of {} with loto number of {} should have returned `True`".format(has_max_of_8, 8)


def test_tuple_first_two_numbers_sum_is_8_will_return_true():
    first_two_numbers_sum_is_8 = [(3, 5, 4), (2, 6, 2, 3, 5), (4, 4, 9, 4, 7)]

    assert assignment2.is_won_loto(first_two_numbers_sum_is_8, 8), \
        "tuple of {} with loto number of {} should have returned `True`".format(first_two_numbers_sum_is_8, 8)


def test_tuple_next_to_last_number_is_always_8_will_return_true():
    next_to_last_number_is_always_8 = [(3, 8, 4), (2, 6, 2, 8, 5), (8, 4)]

    assert assignment2.is_won_loto(next_to_last_number_is_always_8, 8), \
        "tuple of {} with loto number of {} should have returned `True`".format(next_to_last_number_is_always_8, 8)


def test_tuple_only_one_of_the_tuples_have_max_of_8_will_return_false():
    only_one_of_the_tuples_have_max_of_8 = [(3, 5, 4), (2, 8, 2, 3, 5), (4, 9, 8)]

    assert not assignment2.is_won_loto(only_one_of_the_tuples_have_max_of_8, 8), \
        "tuple of {} with loto number of {} should have returned `True`".format(only_one_of_the_tuples_have_max_of_8, 8)


def test_tuple_nothing_is_true_in_this_list_will_return_false():
    nothing_is_true_in_this_list = [(3, 3, 9), (8, 6, 2), (4, 1, 9, 8)]

    assert not assignment2.is_won_loto(nothing_is_true_in_this_list, 8), \
        "tuple of {} with loto number of {} should have returned `True`".format(nothing_is_true_in_this_list, 8)
