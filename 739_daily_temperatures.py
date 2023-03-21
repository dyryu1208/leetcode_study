import time
from typing import List
'''
매일의 화씨온도('F) 리스트 F를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

입력 : 
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    
출력 : 
    [1,1,4,2,1,1,0,0]
'''

def solution(T: List[int]) -> List[int]:
    '''
    스택값 비교
    42_trapping_rainwater 문제와 유사
    
    1. 인덱스를 스택에 쌓기
    2. 이전보다 상승하는 지점에서 인덱스 차이 계산
    '''
    answer = [0] * len(T)
    stack = []
    
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()    # list.pop() 하면 인덱스가 아니라 원소값 리턴되는거 아님? 
            answer[last] = i - last  # 왜 answer[last]가 인덱스로 지정되는지?
        stack.append(i)

    return answer

start = time.time()
T = [73, 74, 75, 71, 69, 72, 76, 73]

for iter in range(10):
    answer = solution(T)
print(time.time() - start)