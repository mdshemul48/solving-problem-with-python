def sortAnArray(arr: list):
    # first a ammra akta variable create korbo jaitai akta empty array thakba.
    # tar por loop deya check korbo ja oitar por kono
    #  element oitar thaka chto ase nake. jodi oitar thaka choto thake thaole oita ar append korbo na.. jodi oitar thaka chtoto na thake
    #  tahole new array ta append kore debo
    loop_counter = 0
    while loop_counter < len(arr):
        for item_index in range(1, len(arr)):
            current_element = arr[item_index]
            prev_element = arr[item_index - 1]
            if current_element < prev_element:
                arr[item_index - 1] = current_element
                arr[item_index] = prev_element
        loop_counter += 1
    return arr


if __name__ == "__main__":
    print(
        sortAnArray(
            [
                50,
                100,
                1,
                5000,
                30,
                45345,
                23423423,
                2121,
                234234234,
                66,
                333243,
                222,
                2,
            ],
        )
    )
