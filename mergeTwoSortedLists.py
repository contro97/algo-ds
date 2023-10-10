# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        print(head.next)
        return head.next

if __name__ == '__main__':
    list1 = ListNode([1, 2, 4])
    list2 = ListNode([1, 3, 4, 5])
    print(list1.val)
    print(list1.next)
    s = Solution
    s.mergeTwoLists(s, list1, list2)

