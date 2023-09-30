# Problem: A sorted array has been rotated so that the elements might appear in the order 3 4 5 6 7 1 2. How would you find the minimum element?

def find_min_value(rotated_array):
    min_value = rotated_array[0]
    i = 0
    while i < len(rotated_array):
        if rotated_array[i] < min_value:
            return rotated_array[i]
        i += 1
    # else
    return rotated_array[0]

# test cases
print(find_min_value([3, 4, 5, 6, 7, 1, 2])) # 1
print(find_min_value([3, 4, 5, 6, 7, 8, 9])) # 3
print(find_min_value([1, 2, 3, 4, 5, 6, 7])) # 1
print(find_min_value([7, 1, 2, 3, 4, 5, 6])) # 1
print(find_min_value([6, 7, 1, 2, 3, 4, 5])) # 1
print(find_min_value([5, 6, 7, 1, 2, 3, 4])) # 1
print(find_min_value([4, 5, 6, 7, 1, 2, 3])) # 1
print(find_min_value([2, 3, 4, 5, 6, 7, 1])) # 1
print(find_min_value([2, 2, 2, 1])) # 1
print(find_min_value([1, 2, 2, 2, 1])) # 1