import time

'''
괄호로 된 입력값이 올바른지 판별하라.

입력 : 
    ()[]{}
    
출력 : 
    True
'''

def solution_1(s: str) -> bool:
    '''
    스택 일치 여부 판별
    아래와 같은 예외처리 필요
    1. table과 s 비교 후, table에 없는 단어가 들어가면 stack에 append
    2. stack이 비었거나, key s 값이 stack.pop()과 다르다면 False 리턴(Error를 발생시키지 않기 위함)
    3. 정상적으로 입력이 들어왔다면 len(stack)은 0일 것이므로 True 리턴
    '''
    stack = []
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }
    
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    
    return len(stack) == 0