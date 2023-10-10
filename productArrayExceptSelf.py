def productArray(nums):
    array_length = len(nums)  # get length of input array
    output_array = [0] * array_length  # create new array of 0-values with length nums

    # calculate prefix products
    prefix_product = 1
    for i in range(array_length):
        output_array[i] = prefix_product
        print("output_array", output_array)
        prefix_product *= nums[i]
        print("prefix_product", prefix_product)

    # calculate the suffix products & multiply with prefix products
    suffix_product = 1
    print("--------")
    for i in range(array_length - 1, -1, -1):
        output_array[i] *= suffix_product
        print("output_array", output_array)
        suffix_product *= nums[i]
        print("suffix_product", suffix_product)

    print(output_array)
    return output_array




if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    productArray(nums)