import time
import collections
from typing import List
'''
연결 리스트가 팰린드롬 구조인지 판별하라

예제 1)

입력 : 
    1->2

출력 : 
    False
    
예제 2)

입력 : 
    1->2->2->1
    
출력 :
    True
'''

# Linked List 생성
class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = None
    

def solution_1(head: ListNode) -> bool:
    '''
    linked_list를 파이썬의 링크 리스트로 변환
    '''
    q: List = []
    
    if not head:
        return True
    
    node = head
    
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    
    return True


def solution_2(head:ListNode) -> bool:
    '''
    Deque를 활용하여 리스트 없이 최적화
    '''
    q: Deque = collections.deque()
    
    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True


def solution_3(head:ListNode) -> bool:
    '''
    런너(Runner) 기법을 활용한 풀이
    런너 기법 -> 연결 리스트 순회 시 2개의 포인터를 동시에 사용하는 기법
               한 포인터(Fast Runner)를 다른 포인터(Slow Runner)보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별시 사용 가능
               Fast Runner가 연결 리스트의 끝에 도달하면, Slow Runner는 정확히 중간 지점에 도달
               이후, 값을 비교
    '''
    rev = None
    slow = fast = head   # 초기값은 head로 동일
    
    while fast and fast.next:      # fast는 두칸씩 이동, slow는 한칸씩 이동
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next   # 역순 연결리스트 rev
    
    if fast:
        slow = slow.next
    
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    return not rev


if __name__ == '__main__':
    list_1 = ListNode(1)
    list_2 = ListNode(2)
    list_3 = ListNode(2)
    list_4 = ListNode(1)
    
    head = list_1
    list_1.next = list_2
    list_2.next = list_3
    list_3.next = list_4
    
    start = time.time()
    
    for iter in range(100):
        solution_3(head)
    print(time.time() - start)
