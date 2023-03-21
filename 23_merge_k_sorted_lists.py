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
    heapq 메서드 사용 -> 원하는 리스트 요소(최소/최대값)을 추출할 수  있음
    heappush : 원하는 요소를 리스트에 삽입 
    heappop : 원하는 요소를 리스트에서 추출
    '''
    root = result = ListNode(None)
    heap = []
    
    for i in range(len(lists)): 
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
    
    while heap:
        node = heapq.heappop(heap)
        idx = node[i]
        result.next = node[2]
        
        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
    
    return root.next