def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lst))
