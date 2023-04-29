def linearize_list(lst):
    result = []
    for elem in lst:
        if isinstance(elem, list):
            result.extend(linearize_list(elem))
        else:
            result.append(elem)
    return result
lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
print(linearize_list(lst))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
