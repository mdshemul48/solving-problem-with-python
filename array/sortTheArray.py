def sortTheArray(arr):
    for _ in range(len(arr)):
        for current_index in range(1, len(arr)):
            if arr[current_index] < arr[current_index - 1]:
                temp = arr[current_index - 1]
                arr[current_index - 1] = arr[current_index]
                arr[current_index] = temp
    return arr


print(sortTheArray([0, 2, 1, 2, 0]))
