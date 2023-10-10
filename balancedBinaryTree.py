def getEfficiency(li):
    s = sum(li)

    if s % 2:
        return -1

    sum_half = s // 2

    skills_dict = {}

    for i in li:

        if skills_dict.get(i):

            skills_dict[i] += 1

        else:

            skills_dict[i] = 1

    res = 0

    for i, j in skills_dict.items():

        key1 = i

        key2 = sum_half - i

        if skills_dict.get(key2):

            if j == skills_dict[key2]:

                res = res + j * (key1 * key2)

            else:

                return -1

        else:

            return -1

    return res // 2



if __name__ == '__main__':
    testList = [6, 2, 1, 1, 4, 3, 4]
    print(getEfficiency(testList))