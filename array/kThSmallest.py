def findKthSmallestNumber(array, k):
    # first a amadar array ka sort korte hobe.
    # then amara sort array thaka index use kore k th element access korte parbo.
    loop_counter = 0
    while loop_counter < len(array):
        for index_of_element in range(1, len(array)):
            if array[index_of_element] < array[index_of_element - 1]:
                temp_element = array[index_of_element]
                array[index_of_element] = array[index_of_element - 1]
                array[index_of_element - 1] = temp_element
        loop_counter += 1
    return array[k - 1]


if __name__ == "__main__":
    print(findKthSmallestNumber([7, 10, 4, 20, 15], 4))
