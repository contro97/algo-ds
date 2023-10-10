def maxArea(nums):

    max_area = 0
    current_area = 0
    l = 0 # left pointer
    r = len(height) - 1 # right pointer
    while l < r:
        current = (r-l)*min(height[l],height[r])
        next1 = (r-l-1)*min(height[l],height[r-1])
        

if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    maxArea(height)