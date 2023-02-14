import time
from typing import List
"""
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

예제 1. ['h', 'e', 'l', 'l', 'o'] -> ['o', 'l', 'l', 'e', 'h']
예제 2. ['H', 'a', 'n', 'n', 'a', 'h'] -> ['h', 'a', 'n', 'n', 'a', 'H']
"""

"""
def reverse_string_dy(string):
    '''
    6_1의 list(reversed(string)) 사용
    '''
    str_to_list_reversed = list(reversed(string))
    print(str_to_list_reversed)

start = time.time()

s = 'Hannah'
# s = 'hello'
reverse_string_dy(s)
print(time.time() - start)
"""

"""
def reverse_string_1(s: List[str]) -> None:
    '''
    투 포인터를 활용한 스왑
    -> 2개의 포인터를 사용해 범위를 조정해가며 변경
    '''
    left, right = 0, len(s)-1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

start = time.time()

s = 'Hannah'
# s = 'hello'
reverse_string_1(s)
print(time.time() - start)
"""


def reverse_string_2(s: List[str]) -> None:
    '''
    위에서 List[str]로 선언 --> list에서만 사용 가능한 list.reverse()
    s = s[::-1]로도 가능하나 코딩 플랫폼마다 오류 가능성 존재
    s[:] = s[::-1]로 변경해서 사용 가능!
    '''
    
    s.reverse()

    print(s)

start = time.time()

s = 'Hannah'
# s = 'hello'
reverse_string_2(list(s))
print(time.time() - start)