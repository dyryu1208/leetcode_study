import time
from typing import List

from matplotlib import collections
'''
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
애너그램 : 문자를 재배열해 다른 뜻을 가진 단어로 바꾸는 것

입력:
    ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    
출력:
    [
        ['ate', 'eat', 'tea'],
        ['nat', 'tan'],
        ['bat']
    ]
'''

def anagram_dy(list_1):
    '''
    https://rollingsnowball.tistory.com/117 참고
    각 리스트 내 단어의 알파벳이 같으면 같은 그룹으로 처리
    ex) ate, eat, tea는 모두 a,t,e를 가짐
    
    1. for 문으로 리스트 내 단어 하나하나 확인  
    2. 개별 단어의 글자순서를 알파벳순으로 정렬
    3. 해당 단어가 없으면 빈 리스트를 생성하고 정렬 전 원래 단어 append
    '''
    result = {}
    
    for word in list_1:
        s = ''.join(sorted(word))
        result[s] = result.get(s, []) + [str]
        print(result)
    


def anagram_1(strs: List[str]) -> List[List[str]]:
    '''
    defaultdict() 사용한게 가장 큰 차이 -> 해당 조건이 없는 경우에도 에러 없이 빈 list 생성 
    '''
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    
    return list(anagrams.values())


start = time.time()

list_1 = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
for iter in range(10):
    anagram_dy(list_1)

print(time.time() - start)
