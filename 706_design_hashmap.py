import time
import collections
'''
다음의 기능을 제공하는 해시맵을 디자인하라.

* put(key, value) : 키, 값을 해시맵에 반영한다. 만약 이미 존재하는 키라면 업데이트한다.
* get(key) : 키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1을 리턴한다.
* remove(key) : 키에 해당하는 키, 값을 해시맵에서 삭제한다.


MyHashMap hashMap = new MyHashMap();
hashMap.put(1,1);
hashMap.put(2,2);
hashMap.get(1);
hashMap.get(3);
hashMap.put(2,1);
hashMap.get(2);
hashMap.remove(2);
hashMap.get(2);
'''
'''
해시 함수 : 임의 크기의 데이터를 고정된 크기 값으로 매핑하는데 쓸 수 있는 함수
         정보를 빠르게 저장하고 검색하기 위해 사용
         파이썬에서는 오픈 어드레싱 방식을 사용해 해시함수 구성하고, 딕셔너리 자료형을 이용
         
ex.   ABC -> A1
ex2.  1324BC -> CB
ex3.  AF32B -> D5
'''

# Linked List 생성
class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = None


class MyHashMap():
    '''
    개별 체이닝 방식을 활용한 해시맵 디자인
    개별 체이닝 방식 : key의 해시값을 계산 -> 해시값을 통해 배열의 인덱스 확인 -> 같은 인덱스가 있는 경우 연결 리스트로 연결
    '''
    def __init__(self):
        '''
        hashmap size : 1000
        table : 존재하지 않는 키를 조회하는 경우 default를 생성하는 defaultdictt 사용
        '''
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
    
    def put(self, key: int, value: int) -> None:
        '''
        index : Modulo연산으로 계산 -> hash table의 가장 기본적인 처리 방식
        if문 ~
        * hash table의 인덱스에 아무 값도 없는 경우 :
            table에 key, value 삽입 후 바로 종료
        
        * 인덱스에 값이 있는 경우(해시 충돌):
            개별 체이닝 방식 사용 -> 연결 리스트로 이어나감    
            1) if p.key == key: --> p의 값을 업데이트
            2) if p.next if None: --> 아무것도 하지 않고 루프 빠져나감 --> 이후 p.next = ListNode(key, value)를 통해 원래 값 유지         
        '''
        index = key % self.size
        
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return 
        
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return 
            
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)
    
    def get(self, key:int) -> int:
        '''
        1) index가 존재하지 않는 경우(key, value가 아예 없는 경우) -> return -1
        2) index가 존재하는 경우 -> 해당하는 값을 출력 
        '''
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
    
    def remove(self, key:int) -> None:
        '''
        1) index가 존재하지 않는 경우 -> 그대로 종료
        2) index가 존재하는 경우 -> index의 첫번째 노드인 경우와 연결리스트 노드인 경우
        '''
        index = key % self.size
        if self.table[index].value is None:
            return 
        
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return 
        
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next