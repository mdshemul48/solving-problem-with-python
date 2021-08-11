# Given an unsorted array arr[] of size N having both negative and
# positive integers. The task is place all negative element at the
# end of array without changing the order of positive element and
# negative element.


# Example 1:

# Input :
# N = 8
# arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
# Output :
# 1  3  2  11  6  -1  -7  -5

# Example 2:

# Input :
# N=8
# arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
# Output :
# 7  9  10  11  -5  -3  -4  -1


# def move_all_negative_to_end(array: list):
#     for _ in array:
#         for item_index in range(0, len(array) - 1):
#             element = array[item_index]
#             if element < 0 and array[item_index + 1] > 0:
#                 temp_element = element
#                 array[item_index] = array[item_index + 1]
#                 array[item_index + 1] = temp_element
#     return array


def move_all_negative_to_end(array: list):
    negative_array = []
    positive_array = []

    for item in array:
        if item < 0:
            negative_array.append(item)
        else:
            positive_array.append(item)
    return positive_array + negative_array


if __name__ == "__main__":
    array = [-8, 9, 5, 10, 2, 6, -7, 7]
    print(move_all_negative_to_end(array))
