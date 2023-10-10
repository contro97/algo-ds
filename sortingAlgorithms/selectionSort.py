import null as null
def selectionSort(array):

    size = len(array)

    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):

            if array[j] < array[min_index]:
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])



    print(array)
    return array

if __name__ == '__main__':
    testArray = [-2, 45, 0, 11, -9,88,-97,-202,747]
    selectionSort(testArray)