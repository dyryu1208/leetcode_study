from typing import List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def create_list(in_list:List[int]) -> ListNode:
    '''
    list를 받아 연결리스트를 생성하는 함수
    '''
    if len(in_list) == 0:
        raise RuntimeError('input list must have data.')
    head_node = ListNode(in_list[0])
    last_node = head_node
    
    for idx in range(1, len(in_list)):
        node = ListNode(in_list[idx])
        last_node.next = node
        last_node = node
    return head_node

def printNodes(node:ListNode):
    '''
    현재까지 만든 LinkedList를 iterative한 방식으로 출력
    crnt_node : 현재 위치로 지정할 노드
    '''
    crnt_node =  node
    while crnt_node is not None:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next
            
def printNodesRecur(node:ListNode):
    '''
    현재까지 만든 LinkedList를 recursive한 방식으로 출력
    '''
    print(node.val, end=' ')
    if node.next is not None:
        printNodesRecur(node.next)

class LinkedList():
    
    def __init__(self):
        self.head = None

    def add_at_head(self, val):
        '''
        LinkedList의 맨 앞부분에 val값이 들어간 노드 추가
        1) 새 노드를 만들고
        2) 새 노드의 next -> head가 가리키던 곳을 넣어줌
        3) head -> node를 가리키게끔
        O(1)
        '''
        node = ListNode(val)
        node.next = self.head
        self.head = node
    
    def add_at_back(self, val):
        '''
        LinkedList의 맨 뒷 부분에 val값이 들어간 노드 추가
        1) 새 node를 만들고
        2) crnt_node가 head부터 차례대로 돌다가
        3) crnt_node의 next가 할당 안됐을때 새 node에 연결
        '''
        node = ListNode(val)
        crnt_node = self.head
        
        while crnt_node.next:
            crnt_node = crnt_node.next
        crnt_node.next = node

    def find_node(self, val):
        '''
        LinkedList의 val에 해당하는 node 찾기
        O(n)
        '''
        crnt_node = self.head
        while crnt_node is not None:
            if crnt_node.val == val:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError('Node not found')
    
    def add_after(self, node, val):
        '''
        특정 노드 뒤에 노드를 추가하는 함수
        1) new_node 만들고
        2) new_node의 next가 node의 next를 가리키게 하고(같은 곳을 가리킴)
        3) node의 next가 new_node를 가리키도록
        O(1)
        '''
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node
    
    def delete_after(self, prev_node):
        '''
        prev_node의 다음 노드를 제거하는 함수
        1) prev_node의 다음 노드가 존재한다면
        2) prev_node를 다음다음(next.next)노드로 연결
        3) 자연스럽게 다음 노드는 연결을 잃고 제거됨
        O(1)
        * 위 방법은 지우고 싶은 노드를 직접 지정하는 것보다 시간복잡도에서 이점
        '''
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next
            
    def recursive(self, node:ListNode):
        '''
        특정 값을 가진 노드를 지우는 방법
        재귀 구조를 이용(iterative한 위 방식을 사용하게 되면 prev_node가 지우고 싶은 element인 경우인 예외 케이스 발생)
        
        '''
        if not node:
            return None
        next_node = self.recursive(node.next)
        if node.val == self.__val:  # 현재 node의 값이 삭제하고자 하는 값이라면
            return next_node        # next_node를 가져와 연결
        else:
            node.next = next_node   # 아니라면 다음 노드 진행
            return node
    
    def iterative(self, node:ListNode):
        '''
        위 방식의 iterative 버전
        앞에 dummy node를 하나 만들어놓고(가상의 prev_node)
        순차적으로 돌면서 제거할 값이 있는 경우 delete_after함수와 같은 방식 사용
        마지막으로 dummy node의 next를 리턴하면 dummy node는 자연스럽게 연결리스트에서 제거
        '''
        dummy_node = ListNode(0)
        dummy_node.next = node
        
        crnt_node = node
        prev_node = dummy_node
        
        while crnt_node:
            if crnt_node.val == self.__val:
                prev_node.next = crnt_node.next
                crnt_node = crnt_node.next
            
            else:
                crnt_node = crnt_node.next
                prev_node = prev_node.next
        return dummy_node.next
    