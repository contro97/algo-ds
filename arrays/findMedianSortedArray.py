def findMedianSortedArray(nums1, nums2):

    newList = nums1 + nums2
    newList.sort()

    size = len(newList)

    print("size", size)
    if size % 2 != 0:
        # get middle index
        middle_index = int((size + 1 )/2)
        print(newList[middle_index -1])
        median = newList[middle_index -1]
        print(median)
        return median


    else:
        idx_1 = int((size + 1 )/2)
        idx_2 = idx_1 - 1

        median = (newList[idx_1] + newList[idx_2])/2

        print("else median",median)
        return median




if __name__ == '__main__':
    list1 = [1,2]
    list2 = [3,4]

    findMedianSortedArray(list1,list2)