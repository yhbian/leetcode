def merge(list1, list2):
    r"""
    :param list1: a sorted list
    :param list2: a sorted list
    :return:
    """
    idx1, idx2 = 0, 0
    merged = []
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] <= list2[idx2]:
            merged.append(list1[idx1])
            idx1 += 1
        else:
            merged.append(list2[idx2])
            idx2 += 1
    if idx1 < len(list1):
        merged.extend(list1[idx1:])
    else:
        merged.extend(list2[idx2:])
    return merged


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    lst1, lst2 = lst[:int(len(lst)/2)], lst[int(len(lst)/2):]
    sorted_lst1 = merge_sort(lst1)
    sorted_lst2 = merge_sort(lst2)
    return merge(sorted_lst1, sorted_lst2)


if __name__ == '__main__':
    lst = [3, 5, 7, 8, 1]
    print(merge_sort(lst))
