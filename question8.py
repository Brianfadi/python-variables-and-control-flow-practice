def dictionary(d, n):
    result = [key for key, value in d.items() if value > n]
    return result

sample_dict = {'a': 5, 'b': 12, 'c': 3}
print(dictionary(sample_dict, 4))
