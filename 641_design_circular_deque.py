import time

'''
다음 연산을 제공하는 원형 데크를 디자인하라.

* MyCircularDeque(k): 데크 사이즈를 k로 하는 생성자
* insertFront() : 데크 처음에 아이템을 추가하고 성공할 경우 true를 리턴한다.
* insertLast() : 데크 마지막에 아이템을 추가하고 성공할 경우 true를 리턴한다.
* deleteFrost() : 데크 처음에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
* deleteLast() : 데크 마지막에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
* getFront() : 데크의 첫번째 아이템을 가져온다. 데크가 비어 있다면 -1을 리턴한다.
* getRear() : 데크의 마지막 아이템을 가져온다. 데크가 비어 있다면 -1을 리턴한다.
* isEmpty() : 데크가 비어 있는지 여부를 판별한다.
* isFull() : 데크가 가득 차 있는지 여부를 판별한다.
'''
# Linked List 생성
class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = None


class MyCircularDeque():
    '''
    Deque : 양쪽 끝을 모두 추출가능한, Queue를 일반화한 형태의 추상자료형(ADT).
            양쪽에서 삭제/삽입을 모두 처리 가능하며, 스택/큐의 특징을 모두 갖고 있음.
            
    이중 연결 리스트를 이용한 데크 구현
    '''
    def __init__(self, k):
        '''
        k : 원형 데크 최대 길이
        self.len : 현재 길이 정보
        '''
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
    
    def insertFront(self, value):
        '''
        앞쪽에 노드를 추가하는 함수
        새로운 노드 삽입 시 최대 길이에 도달하면 False를, 이외에는 _add()함수로 
        head위치에 노드 삽입
        '''
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
    
    def insertLast(self, value):
        '''
        뒤쪽에 노드를 추가하는 함수
        '''
        self._add(self.tail.left, ListNode(value))
        return True
    
    def _add(self, node:ListNode, new:ListNode):
        
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
        
    def _del(self, node:ListNode):
        
        n = node.right.right
        node.right = n
        n.left = node

    
    def deleteFront(self):
        '''
        앞쪽 노드를 제거하는 함수 
        '''
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True


    def deleteLast(self):
        '''
        뒤쪽 노드를 제거하는 함수
        '''
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
    
    
    def getFront(self):
        return self.head.right.value if self.len else -1
    
    def getLast(self):
        return self.tail.left.value if self.len else -1
    
    def isEmpty(self):
        return self.len == 0
    
    def isFull(self):
        return self.len == self.k
        