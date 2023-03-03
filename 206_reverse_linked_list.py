import time

'''
연결 리스트를 뒤집어라

입력 : 
    1->2->3->4->5->NULL
    
출력 :
    5->4->3->2->1->NULL
'''

class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = None

        
def solution_1(head: ListNode) -> ListNode:
    '''
    재귀 구조로 뒤집기
    재귀 구조 : 자기 자신을 호출하여 작업을 반복하는 형식
    
    next : 지정된 노드의 다음노드 (2->3->4->5)
    node.next
    '''
    
    def reverse(node: ListNode, prev: ListNode=None):
        if not node:
            return prev
        
        next, node.next = node.next, prev        

        return reverse(next, node)              

    return reverse(head)

solution_1(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))


def solution_2(head: ListNode) -> ListNode:
    '''
    반복 구조로 뒤집기
    node가 None이 될 때까지 반복
    '''
    node, prev = head, None
    while node:                             # 1번째 루프
        next, node.next = node.next, prev   # next : 2->3->4->5   
        prev, node = node, next             # prev : 1   next -> node : 2->3->4->5
        
                                            # 2번째 루프
                                            # next : 3->4->5
                                            # prev : 2->1    next -> node : 3->4->5
    
    return prev

