'''
스택을 이용해 다음 연산을 지원하는 큐를 구현하라.

push(x) : 요소 x를 큐 마지막에 삽입한다.
pop() : 큐 첫번째 요소를 삭제한다.
peek() : 큐 첫번째 요소를 조회한다.
empty() : 큐가 비어있는지 여부를 리턴한다.

Mystack queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  --> 1 리턴
queue.pop();   --> 1 리턴
queue.empty(); --> false 리턴
'''

class MyQueue():
    '''
    stack은 LIFO 구조이므로, 첫번째 요소 꺼낼때 마지막 원소를 추출해야 함
    pop시 맨 마지막 원소만 계속 추출 후 제거 --> 무한반복의 위험
    2개의 stack을 사용해서 저장
    '''
    def __init__(self):
        self.input = []
        self.output = []
    
    def push(self, x):
        self.input.append(x)
    
    def pop(self):
        self.peek()
        return self.output.pop()
    
    def peek(self):
        '''
        output이 없다면:
            input의 마지막 원소를 output에 입력 후 output 리턴
        '''
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []