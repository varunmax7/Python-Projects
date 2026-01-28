def common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))
print("Common Values: ", common_values([1, 2, 3, 4], [3, 4, 5, 6]))
