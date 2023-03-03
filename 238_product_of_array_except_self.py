import time
from typing import List

'''
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록
출력하라

입력 : 
    [1,2,3,4]

출력 : 
    [24,12,8,6]
    
주의 : 나눗셈을 하지 않고 O(n)에 풀이하라
'''

def solution_dy(nums:List[int]) -> List[int]:
    '''
    1. for문을 돌며 nums에서 idx 요소 제거
    2. 나머지 원소들의 곱 계산 mul
    3. result에 mul append
    '''
    result = []
    for idx, e in enumerate(nums):
        mul = 1
        nums.remove(e)
        for e2 in nums:
           mul *= e2 
        result.append(mul)
        nums.insert(idx,e)
    return result


start = time.time()
nums = [1,2,3,4]

for iter in range(100):
    result = solution_dy(nums)
print(time.time() - start)


def solution_1(nums : List[int]) -> List[int]:
    '''
    자신을 제외하고 왼쪽 곱과 오른쪽 곱을 곱하기
    [1,2,3,4]
    
    p_left = [1,1,2,6]
    p_right = [24,12,4,1]
    '''
    
    out = []
    p = 1
    
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    
    p = 1
    
    for i in range(len(nums)-1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    
    return out

start = time.time()
nums = [1,2,3,4]

for iter in range(100):
    result = solution_1(nums)
print(time.time() - start)



'''
from itertools import accumulate

nums = [1,2,3,4]
results = list(accumulate(nums, lambda x, y : x*y))
'''