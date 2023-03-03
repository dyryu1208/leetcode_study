import time
from typing import List

'''
역순으로 저장된 연결 리스트의 숫자를 더하라

입력 : 
    (2 -> 4 -> 3) + (5 -> 6 -> 4)
    
출력 : 
    7 -> 0 -> 8
    
설명 : 
    342 + 465 = 807
'''


def solution_1():
    '''
    자료형 변환
    
    1. 연결 리스트 뒤집기
    2. 뒤집힌 연결 리스트를 문자열로 이어붙인 다음에 숫자로 변환
    3. 모두 계산 후 다시 연결 리스트로 바꾸기
    '''

class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = None
        

class Solution:
    
    # 연결 리스트 뒤집기
    def reverseList(self, head : ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
    #(3 -> 4 -> 2)
    
    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    # [3, 4, 2]
    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        
        return node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))    # (2->4->3) -> (3->4->2)  --> [3,4,2]
        b = self.toList(self.reverseList(l2))    # (5->6->4) -> (4->6->5)  --> [4,6,5]
        
        resultStr = int(''.join(map(str, a))) + int(''.join(map(str, b)))  # 342+465 = 807
        
        return self.toReversedLinkedList(str(resultStr))  # (7 -> 0 -> 8)


def solution_2(l1: ListNode, l2: ListNode) -> ListNode:
    '''
    전가산기 구현                                 
    '''
    root = head = ListNode(0)
    
    carry = 0
    
    while l1 or l2 or carry:
        sum = 0
        
        if l1 :
            sum += l1.val
            l1 = l1.next
        
        if l2 :
            sum += l2.val
            l2 = l2.next
        
        # 몫(자리올림수)과 나머지(값) 계산
        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next
    return root.next