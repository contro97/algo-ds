def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


# function to find partition position
def partition(array, low, high):

    # choose rightmost element
    pivot = array[high]

    # pointer for greater element
    ind = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # if element is smaller than pivot found
            # swap with the greater element pointed by ind
            ind = ind + 1

            # swapping element at i with element at j
            (array[ind], array[j]) = (array[j], array[ind])

    # swap the pivot element with the greater element specified by i
    (array[ind + 1], array[high]) = (array[high], array[ind + 1])

    # return position from where partition is done
    return ind + 1



if __name__ == '__main__':
    data = [1, 7, 4, 1, 10, 9, -2]
    print("Unsorted Array")
    print(data)

    size = len(data)

    quickSort(data, 0, size - 1)

    print('Sorted Array in Ascending Order:')
    print(data)

