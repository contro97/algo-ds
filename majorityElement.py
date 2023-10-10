def majorityElement(nums):

    nums.sort()
    print(nums)

    answer = nums[len(nums)//2]

    print(len(nums)//2)
    print(answer)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3, 8, 3, 8, 2, 8, 1, 4, 8, 8, ]

    majorityElement(nums)