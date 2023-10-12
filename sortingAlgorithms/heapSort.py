# heapify subtree rooted at index i
# n ~ heap size

def heapify(arr, N, i):
    largest = i # initialize largest position as root node
    l = 2*i + 1 # left = 2*i + 1
    r = 2*i +2 # right = 2*i + 2

    # see if left child of root exists and is greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # see if right child exists and is greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap

        # heapify the root
        heapify(arr, N, largest)


def heapSort(arr):
    N = len(arr)

    # build a maxheap
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i , 0)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]

    # Function call
    heapSort(arr)
    N = len(arr)

    print("Sorted array is")
    for i in range(N):
        print("%d" % arr[i], end=" ")