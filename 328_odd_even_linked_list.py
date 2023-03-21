import time

from requests import head

'''
연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.

입력 : 
    1 -> 2 -> 3 -> 4 -> 5 -> NULL
    2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7 -> NULL

출력 : 
    1 -> 3 -> 5 -> 2 -> 4 -> NULL
    2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4 -> NULL
'''

class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = None


def solution_1(Node: ListNode) -> ListNode:
    '''
    반복 구조로 홀짝 노드 처리
    
    홀, 짝의 각 노드 구성 후 홀수 노드의 마지막을 짝수 노드의 처음과 잇기
    '''
    if head is None:
        return None
    
    odd = head
    even = head.next
    even_head = head.next
    
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
    
    odd.next = even_head
    return head