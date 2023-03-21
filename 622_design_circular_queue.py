'''
원형 큐를 디자인 하라.

MyCircularQueue     circularQueue = new MyCircularQueue(5);   // 크기를 5로 지정
circularQueue.enQueue(10);   // true 리턴
circularQueue.enQueue(20);   // true 리턴
circularQueue.enQueue(30);   // true 리턴
circularQueue.enQueue(40);   // true 리턴
circularQueue.Rear();        // 40 리턴
circularQueue.isFull();      // false 리턴
circularQueue.deQueue();     // true 리턴
circularQueue.deQueue();     // true 리턴
circularQueue.enQueue(50);   // true 리턴
circularQueue.enQueue(60);   // true 리턴
circularQueue.Rear();        // 60 리턴
circularQueue.Front();      //  30 리턴
'''

class MyCircularQueue():
    '''
    원형 큐 : 삭제 후 충분한 공간이 앞쪽에 남는다면 이를 재활용 가능하게 만드는 구조
    front, rear 포인터 존재
    enQueue : 요소를 추가
    deQueue : 요소를 삭제
    Front : 맨 앞 요소 조회
    Rear : 맨 뒤 요소 조회
    isFull : 원형 큐가 꽉 찼는지 확인
    '''
    def __init__(self, k):
        '''
        k : 원형 큐 size
        p1 : front point
        p2 : rear point
        '''
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
    
    def enQueue(self, value):
        '''
        1. p2위치에 값 삽입
        2. p2를 한칸 뒤로 이동 및 최대길이(k) 넘지 않도록
        '''
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        
        else: 
            return False
    
    def deQueue(self):
        '''
        1. 기존 p1위치 값을 삭제
        2. p1을 한칸 뒤로 이동 및 최대길이(k) 넘지 않도록
        '''
        if self.q[self.p1] is None:
            return False
        
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
            
    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    
    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]    
    
    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None
    
    
circularQueue = MyCircularQueue(5);
print(circularQueue.enQueue(10));   #// true 리턴
print(circularQueue.enQueue(20));   #// true 리턴
print(circularQueue.Front());      #//  10 리턴
print(circularQueue.enQueue(30));   #// true 리턴
print(circularQueue.enQueue(40));   #// true 리턴
print(circularQueue.Rear());        #// 40 리턴
print(circularQueue.isFull());      #// false 리턴
print(circularQueue.deQueue());     #// true 리턴
print(circularQueue.deQueue());     #// true 리턴
print(circularQueue.enQueue(50));   #// true 리턴
print(circularQueue.enQueue(60));   #// true 리턴
print(circularQueue.Rear());        #// 60 리턴