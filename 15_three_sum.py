import time
from typing import List

'''
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라

입력 : 
    nums = [-1, 0, 1, 2, -1,-4]
    
출력 : 
    [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
'''

def three_num_sum_dy(nums: List[int]) -> List[int]:
    '''
    3포인터 사용하여 배열 내 모든 조합 생성
    
    1. e1, e2, e3 = 0, 1, 2에 위치시키고
    2. e3을 제일 먼저 오른쪽으로 한칸씩 움직임
    3. e2, e3을 한칸씩 오른쪽으로 밀어냄
    4. e2, e3가 제일 오른쪽까지 갔다면
    5. e1, e2, e3를 한칸씩 오른쪽으로 이동
    
    생성된 result를 오름차순 정렬 후 중복 제거
    '''
    result = []
    e1, e2, e3 = 0, 1, 2
    
    while e1 != len(nums)-2:
        while e2 != len(nums)-1:
            while e3 != len(nums):
                if nums[e1] + nums[e2] + nums[e3] == 0:
                    result.append([nums[e1], nums[e2], nums[e3]])
                e3 += 1
            e2 += 1
            e3 = e2+1
        e1 += 1
        e2 = e1+1
        e3 = e2+1
    
    answer = []
    for arr in result:
        arr.sort()
        if arr not in answer:
            answer.append(arr)
    
    return answer



def three_num_sum_1(nums:List[int]) -> List[List[int]]:
    '''
    Brute-Force 계산(위 방식과 비슷)
    * 오름차순으로 sorting | 중복제거 로직이 차이점
    '''
    results = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i+1, len(nums)-1):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue
                
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
    return results


def three_num_sum_2(nums:List[int]) -> List[int]:
    '''
    투 포인터 활용
    i의 다음 지점을 left, 맨 마지막 지점을 right로 설정
    설정 후 간격을 좁히며 sum
    sum < 0 -> left를 우측으로 이동
    sum > 0 -> right를 좌측으로 이동
    '''
    results = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0 :
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])
                
                # 동일한 값이 있는 경우 패스하는 로직
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
    return results

start = time.time()
nums = [-1, 0, 1, 2, -1, -4]

for iter in range(10):
    result = three_num_sum_dy(nums)

print(time.time() - start)
print(result)  
