import time
import heapq
from typing import List
'''
k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.
* 예제의 k=3
입력 : 
    [
        1->4->5,
        1->3->4,
        2->6
    ]
    
출력 : 
    1->1->2->3->4->4->5->6
'''

# Linked List 생성
class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = None

def mergeKLists(lists:List[ListNode]):
    '''
    heapq 메서드 사용 -> 원하는 리스트 요소(최소/최대값)을 추출가능
    heappush : 원하는 요소를 리스트에 삽입
    heappop : 원하는 요소를 리스트에서 추출
    ''' 
    root = result = ListNode(None)
    heap = []
    
    for i in range(len(lists)):   
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i])) # 중복된 lists 인자를 push 하기위해 heappush 내 추가 인자 삽입
    
    while heap:
        # 리스트 내 while문을 돌며 가장 작은 요소를 heappop
        node = heapq.heappop(heap)   
        idx = node[i]
        result.next = node[2]
        
        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
    return root.next