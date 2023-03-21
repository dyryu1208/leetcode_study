import time
from collections import deque
'''
큐를 이용해 다음 연산을 지원하는 스택을 구현하라.

push(x) : 요소 x를 스택에 삽입한다.
pop() : 스택의 첫번째 요소를 삭제한다.
top() : 스택의 첫번째 요소를 가져온다.
empty() : 스택이 비어있는지 여부를 리턴한다.

Mystack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   --> 2 리턴
stack.pop();   --> 2 리턴
stack.empty(); --> false 리턴
'''

class MyStack():
    '''
    기본 queue는 데크로 정의하고, queue 기능을 함수로 추가
    1) push : 
        queue는 FIFO 구조이므로, push함수로 들어온 원소 x를 맨 앞에 정렬
    '''
    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        self.q.append(x)
        
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0