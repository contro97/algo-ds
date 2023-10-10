def insertionSort(arr):

    length = len(arr)

    for i in range(1, length):
        key = arr[i]

        j = i - 1
        print("i-th pass: ", i)
        while j >= 0 and key < arr[j]:


            arr[j+1] = arr[j]

            print(arr[j+1])
            j -= 1
        arr[j + 1] = key
        print(arr[j+1])


if __name__ == '__main__':
    data = [3, 7, 4, 1, 10, 9, 2]

    insertionSort(data)