def find_frequency(array, item):
    total_frequency = 0
    for element in array:
        if item == element:
            total_frequency += 1
    return total_frequency


if __name__ == "__main__":
    result = find_frequency(
        [
            1,
            12,
            2,
            2,
            2,
            2,
            2,
            1,
            1,
            1,
            2,
            2,
            3,
        ],
        12,
    )
    print(result)
