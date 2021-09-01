def sortTheArray(arr: list):
    for i in range(1, len(arr)):
        currentItem = arr[i]
        prevIndex = i - 1
        while prevIndex >= 0 and currentItem < arr[prevIndex]:
            arr[prevIndex + 1] = arr[prevIndex]
            prevIndex -= 1
        arr[prevIndex + 1] = currentItem

    return arr


def main():
    arr = [1, 4, 5, 2, 3, 10, 8, 40, 20, 15]
    print(sortTheArray(arr))


if __name__ == "__main__":
    main()
