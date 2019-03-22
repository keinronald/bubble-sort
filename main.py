#!/usr/bin/env python3


def my_sort(array):
    """Sorts the values of the array in increasing order using the bubble sort."""
    length = len(array)

    while True:
        swapped = False

        for i in range(0, length-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True

        if swapped == False:
            break

        length = length - 1

    return array


def is_sorted(array):
    """Checks if the values of the array are sorted."""
    if array == sorted(array):
        return True
    return False


if __name__ == "__main__":                     # If called from interpreter
    to_sort = [12, 23, 45, 65, 1, 13, 43, 24, 3]

    print("### Bubble Sort ###")
    print("--- unsorted ---")
    print("array to sort:", to_sort)
    print("sorted?", is_sorted(to_sort))
    print()

    my_sort(to_sort)
    print("--- sorted ---")
    print("sorted:", to_sort)
    print("sorted?", is_sorted(to_sort))

