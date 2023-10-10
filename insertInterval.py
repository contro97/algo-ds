def insert(intervals, newInterval):
    s = newInterval[0]
    e = newInterval[1]
    left = []
    right = []

    for i in intervals:
        if i[1] < s:
            left += i
        elif i[0] > e:
            right += i
        else:
            s = min(s, i[0])
            e = max(e, i[1])

    return left + [[s, e]] + right



if __name__ == '__main__':
    testCase1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    testCase2 = [3, 4]

    print(insert(testCase1, testCase2))