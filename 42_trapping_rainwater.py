import time
from typing import List
'''
높이를 입력받아 비온 다음 얼마나 많은 물이 쌓일 수 있는지 계산하라.

입력 : 
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

출력 : 
    6
'''


def trapping_rainwater_dy(list_h):
    '''
    해당 배열의 순서를 고려 -> 인덱스 2번 건너뛴 순서와의 차이 계산
    인덱스[3] - 인덱스[1] = 2 - 1 = 1
    인덱스[4] - 인덱스[2] = 1 - 0 = 1
    이와 같이 차이 합산하니 합이 6
    투 포인터로 접근
    투 포인터를 오른쪽으로 하나씩 옮겨 가며 덧셈
    --> 높이 배열을 바꿔보니 오답임을 확인...
    '''    
    sum = 0
    left, right = 0, 2
    while not right == len(list_h)-1 :
        if (list_h[right] - list_h[left]) > 0:
            sum += (list_h[right] - list_h[left])
        left += 1
        right += 1
    return sum
            
            
def trapping_rainwater_1(height: List[int]) -> int:
    '''
    투 포인터를 활용
    
    1. 투 포인터 left, right 설정
    2. left_max, right_max 설정 -> 두 포인터의 최고 높이
    3. 중앙으로 이동하며(left+=1, right+=1) left_max, right_max 업데이트(max함수 사용)
    4. volume(물의 양)은 현재 포인트(left, right)의 높이와 left_max, right_max 간 차로 계산
    '''
    
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(right_max, height[right])

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        
        else:
            volume += right_max - height[right]
            right -= 1
    return volume



def trapping_rainwater_2(height):
    '''
    스택쌓기 방식
    스택(Stack) : 그림의 검은색 부분
    오른쪽으로 포인트를 옮겨가며 높이만큼 스택을 쌓는다고 생각!
    
    <while문의 break 요소>
    1. while stack and height[i] > height[stack[-1]]
    
       while stack -> 생성된 리스트 stack이 non-empty 할때까지 반복하겠다
       while stack and height[i] > height[stack[-1]]
       => stack이 non-empty하고 현재 포인트의 높이 > 직전 포인트의 높이인 경우에만 아래 연산을 시행하겠다!
       
    2. top = stack.pop() -> stack의 맨 마지막 요소 제거 & top에 저장
       => 바로 직전 시점 스택의 높이
    3. if not len(stack): break -> stack이 empty하면 break
    '''
    stack = []
    volume = 0
    
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:     # 1. while stack -> stack이 non-empty & 직전포인트보다 현재 포인트 높이가 커야!
            top = stack.pop()            # 2. stack.pop() -> stack의 맨 마지막 요소 제거 & top에 저장
            
            if not len(stack):           # 3. stack이 empty하면 break
                break
            
            # empty하지 않다면 아래 계산 수행
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            
            volume += distance * waters
        
        stack.append(i)
    
    return volume

start = time.time()    
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

trapping_rainwater_2(height)
print(time.time() - start)