import time

'''
연결 리스트를 입력받아 페어(Pair) 단위로 스왑하라.

입력 : 
    1 -> 2 -> 3 -> 4
    
출력 : 
    2 -> 1 -> 4 -> 3
'''

class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = None
        

def solution_1(head: ListNode) -> ListNode:
    '''
    연결 리스트 노드는 그대로 유지하되, val만 변경
    '''
    cur = head
    
    while cur  and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next
        
    return head


def solution_2(head: ListNode) -> ListNode:
    '''
    반복구조를 이용한 swap
    '''
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head
        
        prev.next = b
        
        head = head.next
        prev = prev.next.next
    
    return root.next


def solution_3(head: ListNode) -> ListNode:
    '''
    재귀 구조로 swap
    '''
    if head and head.next:
        p = head.next
        head.next = solution_3(p.next)
        p.next = head
    return head