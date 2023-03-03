import sys
import time
from typing import List

'''
한번의 거래로 낼 수 있는 최대 이익을 산출하라

입력 : 
    [7,1,5,3,6,4]
    
출력 : 
    5
    
설명 : 
    1일때 사서 6일떄 팔면 5의 수익을 거둔다
'''

def solution_dy(prices:List[int])-> int:
    '''
    1. nums.pop(0) -> 리스트 첫번째 요소를 매번 제거하고, 그 값을 e1에 저장
    2. 나머지 원소들에 대해 e2-e1 값이 양수면 profit에 append
    3. profit의 최대값 리턴
    '''
    profit = []
    for e1 in prices:
        e1 = prices.pop(0)
        for e2 in prices:
            if e2 > e1:
               profit.append(e2-e1)
        
    return max(profit)


def solution_1(prices:List[int]) -> int:
    '''
    Brute-Force로 사고팔기 반복
    '''
    max_price = 0
    
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)
    
    return max_price if max_price > 0 else 0


def solution_2(prices : List[int]) -> int:
    '''
    저점과 현재 값과의 차이 계산
    sys.maxsize -> 시스템이 지정가능한 최댓값 리턴
    '''
    
    profit = 0
    min_price = sys.maxsize
    
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    
    return profit

start = time.time()
prices = [7,1,5,3,6,4]

profit = solution_2(prices)
print(time.time() - start)
print(profit)