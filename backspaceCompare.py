class Solution(object):
    def backspaceCompare( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        typed_stk = []
        delete_stk = []

        for i in s:
            if i == '#':
                typed_stk.pop()
            else:
                typed_stk.append(i)

        for i in t:
            if i == '#':
                delete_stk.pop()
            else:
                delete_stk.append(i)

        return typed_stk == delete_stk


if __name__ == '__main__':
    s = "ab##"
    t = "c#d"
    print(Solution.backspaceCompare( s, t))


    print(range(len(s)))
    for i in range(len(s)):
        print(i)
