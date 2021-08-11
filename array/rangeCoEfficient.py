arr = [15, 16, 10, 9, 6, 7, 17]


def find_range_coefficient(arr: list):
    max = 0
    min = arr[0]

    for item in arr:
        if item > max:
            max = item
        elif item < min:
            min = item
    print("range: ", max - min)
    print("coefficient", (max - min) / (max + min))


if __name__ == "__main__":
    find_range_coefficient(arr)
