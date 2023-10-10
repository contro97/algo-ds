# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def twoSum(nums, target):

    num_dict = {} # create dictionary to store value, index

    for i, num in enumerate(nums):
        complement = target - num
        print("Number Dictionary:", num_dict)
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3, 0, 5, 9, 3]
    target = 6
    print(twoSum(nums, target))

