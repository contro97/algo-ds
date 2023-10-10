def twoSum(nums, target):

    num_dict = {} # create dictionary to store key-value index's of complement

    for i, num in enumerate(nums): # index, value for-loop\
        print("i:", i,"num:", num,)
        complement = target - num # get complement of each value
        if complement in num_dict:
            return [num_dict[complement], i] # kill loop when complement found

        num_dict[num] = i # assign value of complement key-value to position in array



if __name__ == '__main__':
    nums = [3, 1, 0, 0, 0, 0, 3]
    target = 6
    print(twoSum(nums, target))