import time
from typing import List
'''
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

입력 : 
    nums = [2, 7, 11, 15], target = 9

출력 : 
    [0, 1]
'''
def twonum_sum_dy(nums:list, target:int) -> list:
    '''
    for문 2개 돌리기(단순...)
    '''
    for element_1 in nums:
        for element_2 in nums[1:]:
            if element_1 + element_2 == target:
                return [nums.index(element_1), nums.index(element_2)]


def twonum_sum_1(nums: List[str], target: int) -> List[int]:
    '''
    위의 내 풀이와 거의 동일
    -> Brute-Force 계산
    '''
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


def twonum_sum_2(nums: List[str], target: int) -> List[int]:
    '''
    target식의 첫번째 값을 뺀 값 target-n이 존재하는지 확인하는 함수
    다 연산하는 게 아닌, in을 사용해 탐색하므로 시간 복잡도 크게 감소
    
    1) 첫번째 반복이므로 n=2
    2) complement=7
    3) complement가 nums의 1번 인덱스부터 있는지 탐색
    4) n의 인덱스 및 탐색한 인덱스 리턴
    '''
    for i, n in enumerate(nums):
        complement = target - n
        
        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]



def twonum_sum_3(nums: List[int], target: int) -> List[int]:
    '''
    1. key를 숫자, value를 인덱스로 하는 딕셔너리 생성
    2. target - 첫번째 수 계산
    3. 계산한 결과(key)를 딕셔너리에서 찾아 인덱스(value) 리턴
    '''
    nums_map = {}
    
    for idx, num in enumerate(nums):
        nums_map[num] = idx
    
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            return [i, nums_map[target - num]]
        


def twonum_sum_4(nums: List[int], target: int) -> List[int]:
    '''
    투 포인터를 이용하여 문제 해결
    왼쪽 포인터를 맨 처음 인덱스에, 오른쪽 포인터를 마지막 인덱스에 배정
    nums가 오름차순 정렬임을 활용
    왼쪽 포인터 + 오른쪽 포인터 합 < target -> 왼쪽 포인터를 오른쪽으로 한칸 이동
    왼쪽 포인터 + 오른쪽 포인터 합 > target -> 오른쪽 포인터를 왼쪽으로 한칸 이동
    '''
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

nums = [2, 7, 11, 15]
target = 9
    
start = time.time()

for iter in range(10):
    twonum_sum_3(nums, target)
print(time.time() - start)