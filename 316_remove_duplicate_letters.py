from itertools import count
import time
from collections import Counter
'''
중복된 문자를 제외하고 사전식 순서로 나열하라.

입력 : 
    'bcabc'
    'cbacdcbc'
    
출력 :
    'abc'
    'acdb'
'''

def solution_dy(s: str) -> str:
    '''
    1. set으로 중복 제거
    2. sorted로 정렬
    3. string 변환
    
    --> 해당 풀이는 오답이며, 사전식 순서로 나열한다는 점이 간과됨
    * 사전식 순서 : 단어가 중복이 아니면서 앞에 있는 경우 해당 단어의 위치를 그대로 유지
    
    ex) ebcabc -> eabc
    '''
    return ''.join(sorted(set(s)))
    

def solution_1(s: str) -> str:
    '''
    재귀를 이용한 분리
    조건문을 통과하면 글자를 분리하도록 재귀 구조 설정
    '''
    
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + solution_1(suffix.replace(char,''))
    
    return ''


def solution_2(s: str) -> str:
    '''
    스택을 이용한 문자 제거
    counter : 글자별 단어에 등장하는 횟수
    seen : 글자 집합
    stack : 스택 리스트
    
    * while stack and ~ 구문
    
    1) while stack : stack이 빈 리스트가 아닐때
    2) char < stack[-1] : char의 ascii값이 stack의 마지막 요소보다 작을때
                          ascii값 : a -> z로 갈수록 커짐
                                   a < b < c < d ...
    3) counter[stack[-1]] > 0 : stack[-1]의 등장 횟수가 0보다 큰 경우
    
    해당 코드를 축약하면 --> 뒤에 붙일 문자가 남아 있다면 stack에서 앞 문자를 제거
                        ex. bcabc --> abc
    '''
    counter, seen, stack = Counter(s), set(), []
    
    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    
    return ''.join(stack)

string = 'cbacdcbc'
a = solution_2(string)
print(a)