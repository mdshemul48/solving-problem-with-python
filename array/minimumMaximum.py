def getMinMax(a, n):
    maximum = 0
    minimum = a[0]
    item_index = 0
    while item_index < n:
        if a[item_index] > maximum:
            maximum = a[item_index]
        elif a[item_index] < minimum:
            minimum = a[item_index]
        item_index += 1
    return [maximum, minimum]


print(getMinMax([1, 345, 234, 21, 56789], 5))
