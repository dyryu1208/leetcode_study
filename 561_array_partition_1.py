import time
from typing import List
'''
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

입력 : 
    [1,4,3,2]
    
출력 : 
    4
    
설명 : 
    min(1,2) + min(3,4) => 4

겹치지 않게 min(a,b)를 생성한 다음 더하면 될 듯!
'''

def solution_1(nums : List[int]) -> int:
    '''
    1. 리스트를 오름차순으로 정렬
    [1,4,3,2] -> [1,2,3,4]
    2. 인접 요소 페어 생성
    '''
    sum = 0
    pair = []
    nums.sort()
    
    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


def solution_2(nums:List[int]) -> int:
    '''
    짝수 번째 값 계산
    짝수번째 인덱스에 항상 작은 값이 위치 -> 이들을 더하기만 하면 됨!
    불필요한 페어 리스트 생성할 필요 없음
    '''
    sum = 0
    nums.sort()
    
    for idx, n in enumerate(nums):
        if idx % 2 == 0:
            sum += n
    return sum


def solution_3(nums:List[int]) -> int:
    '''
    위 solution_2를 한 줄로 해결 가능
    '''
    return sum(sorted(nums)[::2])


start = time.time()
nums = [1,4,3,2]

for iter in range(10):
    solution_3(nums)
print(time.time() - start)
