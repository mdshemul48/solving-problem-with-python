# Cyclically rotate an array by one
# Given an array, rotate the array by one position in clock-wise direction.

# Example 1:

# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 5 1 2 3 4


# Example 2:

# Input:
# N = 8
# A[] = {9, 8, 7, 6, 4, 2, 1, 3}
# Output:
# 3 9 8 7 6 4 2 1


def rotate_an_array(number_of_array: list):
    index = len(number_of_array) - 1

    while index > 0:
        temp = number_of_array[index]
        number_of_array[index] = number_of_array[index - 1]
        number_of_array[index - 1] = temp
        index -= 1
    return number_of_array


if __name__ == "__main__":
    print(rotate_an_array([1, 2, 3, 4, 5]))
