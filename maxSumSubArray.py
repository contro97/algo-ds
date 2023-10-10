def maxSumSubArray(nums):

    max_sum = nums[0]
    current_sum = 0

    for i in range(len(nums)):
        print(max_sum)
        if current_sum < 0:
            current_sum = 0
        current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

if __name__ == '__main__':
    nums = [1,-4,3,5,-7,2,5]
    print(maxSumSubArray(nums))

