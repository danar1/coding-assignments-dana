#                  DO NOT EDIT!                       #
#  this is a test file that verifies the assignments  #
#    was submitted according to the requirements      #
from session1.src import assignment1


def test_expect_genesis_album_name():
    list1 = [84, 101, 108, 109, 32, 105, 115, 100, 119, 32, 110, 98, 111, 100, 97]
    list2 = [104, 32, 97, 98, 108, 101, 32, 111, 110, 111, 32, 114, 97, 119, 121]

    assert assignment1.convert_number_lists_to_text(list1, list2) == "The lamb lies down on broadway"


def test_expect_a_few_good_man_colonel_jessup_sentence():
    list1 = [89, 117, 119, 110, 32, 110, 119, 114, 63, 32, 32, 97, 116, 116, 101, 116, 117, 104, 32, 111, 32, 97, 39,
             32, 97, 100, 101, 116, 101, 116, 117, 104]
    list2 = [111, 32, 97, 116, 97, 115, 101, 115, 33, 73, 119, 110, 32, 104, 32, 114, 116, 33, 89, 117, 99, 110, 116,
             104, 110, 108, 32, 104, 32, 114, 116, 33]

    assert assignment1.convert_number_lists_to_text(list1, list2) == \
           "You want answers?! I want the truth! You can't handle the truth!"


def test_expect_winston_churchill_quote():
    list1 = [73, 32, 111, 32, 114, 32, 111, 110, 32, 104, 111, 103, 32, 101, 108, 32, 101, 112, 103, 105, 103, 46]
    list2 = [102, 121, 117, 97, 101, 103, 105, 103, 116, 114, 117, 104, 104, 108, 44, 107, 101, 32, 111, 110, 46, 46]

    assert assignment1.convert_number_lists_to_text(list1, list2) == \
           "If you are going through hell, keep going..."


def test_expect_lorem_ipsum_sentence():
    list1 = [76, 114, 109, 105, 115, 109, 100, 108, 114, 115, 116, 97, 101, 32, 111, 115, 99, 101, 117, 32, 100, 112,
             115, 105, 103, 101, 105]
    list2 = [111, 101, 32, 112, 117, 32, 111, 111, 32, 105, 32, 109, 116, 99, 110, 101, 116, 116, 114, 97, 105, 105, 99,
             110, 32, 108, 116]

    assert assignment1.convert_number_lists_to_text(list1, list2) == \
           "Lorem ipsum dolor sit amet consectetur adipiscing elit"


def test_convert_string():
    str_to_convert = "wakawaka"

    assert (len(str_to_convert) % 2) == 0, "String must be of even character number"

    ords = [ord(word) for word in str_to_convert]
    list1 = ords[::2]
    list2 = ords[1::2]

    print("\nList1: ", list1)
    print("List2: ", list2)


