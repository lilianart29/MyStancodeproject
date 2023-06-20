"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    #######################
    d1 = {}
    d2 = {}
    cur1 = l1
    cur2 = l2
    a = 1
    while cur1 is not None:
        d1[a] = cur1.val
        a += 1
        cur1 = cur1.next
    b = 1
    while cur2 is not None:
        d2[b] = cur2.val
        b += 1
        cur2 = cur2.next
    ans = ListNode()
    cur = ans
    if a < b:
        for j in range(b-a):
            d1[a+j] = 0
    if b < a:
        for k in range(a-b):
            d2[b+k] = 0
    for num1, count1 in d1.items():
        for num2, count2 in d2.items():
            if num1 == num2:
                num3 = count1 + count2
                cur.next = ListNode(num3, None)
                cur = cur.next
    ans = ans.next
    ans_tra = []
    cur = ans
    while cur is not None:
        ans_tra.append(cur.val)
        cur = cur.next
    for i in range(len(ans_tra)):
        if ans_tra[i] >= 10:
            if i == len(ans_tra)-1:
                ans_tra[i] = ans_tra[i] - 10
                ans_tra.append(1)
            else:
                ans_tra[i] = ans_tra[i] - 10
                ans_tra[i + 1] += 1
    ans_s = ListNode()
    cur = ans_s
    for i in range(len(ans_tra)):
        cur.next = ListNode(ans_tra[i], None)
        cur = cur.next
    return ans_s.next



####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
