def find_the_key_in_segment(numberArray: list, key: int, segment: int):
    # akta while loop ar moda amaka potibar n ta kore item assess korbo
    # then check korbo ja oi n item item ar moda k number ase nake.
    # jodi thake thaole akta variable a akta string thakba jaiga yes ba no korbo.
    # then loop sas hoyla oi variable return kore debo

    result = "No"
    segment_start = 0
    segment_end = segment
    run_the_loop = True
    while run_the_loop:
        for item_index in range(segment_start, segment_end):
            try:
                currentElement = numberArray[item_index]
                if currentElement == key:
                    result = "Yes"
                    break
            except IndexError:
                run_the_loop = False
                break

        if result != "yes":
            break

        segment_start = segment_end
        segment_end += segment
    return result


if __name__ == "__main__":
    # test 1
    array = [3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3]
    result = find_the_key_in_segment(array, 3, 3)
    print(result)

    # test 2
    array2 = [21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25]
    result2 = find_the_key_in_segment(array2, 23, 5)
    print(result2)

    # test 3
    array3 = [5, 8, 7, 12, 14, 3, 9]
    result3 = find_the_key_in_segment(array2, 8, 2)
    print(result3)
