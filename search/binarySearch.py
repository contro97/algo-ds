def binarySearch(target, array):

    left = 0
    right = len(array) - 1

    while left <= right:
        midpoint = ((left + right)//2)
        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] < target:
            left = midpoint + 1
        else:
            left = midpoint - 1

    return -1


if __name__ == '__main__':
    root = [-1,0,3,5,9,12]
    target = 4
    binarySearch(target, root)
