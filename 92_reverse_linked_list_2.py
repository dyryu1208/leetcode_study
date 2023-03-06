import time

'''
인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.

입력 : 
    1 -> 2 -> 3 -> 4 -> 5 -> NULL.    m = 2, n = 4
    
출력 : 
    1 -> 4 -> 3 -> 2 -> 5 -> NULL
'''

class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = None


def solution_1(head: ListNode, m: int, n: int) -> ListNode:
    '''
    반복 구조로 노드 뒤집기
    '''
    if not head or m == n:
        return head
    
    root = start = ListNode(None)
    root.next = head
    
    for _ in range(m-1):
        start = start.next
    
    end = start.next
    
    for _ in range(n-m):
        temp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = temp
    
    return root.next