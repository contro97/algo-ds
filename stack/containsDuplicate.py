from collections import Counter

def containsDuplicateSetLogic(nums):
    num_set = set()
    for i in nums:
        if i in num_set:
            return True
        num_set.add(i)
        print(num_set)

def containsDuplicateCounterLogic(nums):
    num_counts = Counter(nums) # dictionary that counts values of an occuring value in array
    for count in num_counts.values():
        if count > 1:
            return True
    return False

def containsDuplicateDictionaryLogic():
    num_dict = {}
    for num in nums:
        if num in num_dict:
            return True
        num_dict[num] = 1
    return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    containsDuplicateSetLogic(nums)
