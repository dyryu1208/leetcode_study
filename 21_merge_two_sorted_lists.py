import time

'''
정렬되어 있는 두 연결 리스트를 합쳐라

입력 : 
    1->2->4, 1->3->4

출력 : 
    1->1->2->3->4->4
'''

class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = None
        

def solution_1(l1: ListNode, l2: ListNode) -> ListNode:
    '''
    재귀 구조로 연결
    l1, l2의 값을 비교해 작은 값이 왼쪽에 오게 함
    비교 연산을 먼저 수행하고, not l1 확인
    next로 그 다음 값이 엮이도록 함
    '''
        
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    
    if l1:
        l1.next = solution_1(l1.next, l2)
    
    return l1

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


answer = solution_1(l1, l2)

while answer is not None:
    print(f'{answer.val} -> ', end=' ')
    answer = answer.next  