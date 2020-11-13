def convert_number_lists_to_text(list1, list2):
    """
    This function get two lists that contain numbers
    Converts each number into its ascii representation
    and joins the strings based on their matching index
    return: joined string
    """
    list1_chr = map(chr, list1)
    list2_chr = map(chr, list2)
    tuple_pairs = zip(list1_chr, list2_chr)
    tuple_pairs_sum = sum(tuple_pairs, ())
    res = ''.join(tuple_pairs_sum)
    return res


if __name__ == '__main__':
    list1 = [79, 115, 99, 111, 108, 114, 99, 115, 97, 115]
    list2 = [112, 83, 104, 111, 32, 111, 107, 116, 114, 33]

    print(convert_number_lists_to_text(list1, list2))
