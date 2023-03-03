from email.policy import default
import re
import time
import collections
"""
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구별하지 않으며, 영문자/숫자만을 대상으로 한다
팰린드롬 : 앞뒤로 뒤집어도 똑같은 말이 되는 단어 / 문장

예제 1) A man, a plan, a canal: Panama  -> True
예제 2) race a car -> False
"""


def palindrome_dy(string):
    '''
    본인 시도 결과물
    
        1. 영문자/숫자만 남게 전처리한 cleaned_string 생성
        2. 해당 string 리스트화(str_to_list) & 순서를 바꾼 리스트(str_to_list_reversed) 2개 생성
        3. 빈 리스트(check_list) 1개 생성
        4. str_to_list_reversed의 원소를 뽑아 check_list에 투입
        5. check_list == str_to_list 여부 확인
    '''
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    str_to_list = list(cleaned_string)
    str_to_list_reversed = list(reversed(str_to_list))
    check_list = []
    
    for word in range(len(str_to_list_reversed)):
        check_list.append(str_to_list_reversed[word])

    if check_list == str_to_list:
        print(True)
    else:
        print(False)
        
start = time.time()
string = 'A man, a plan, a canal: Panama'
#string = 'race a car'
palindrome_dy(string)
print(time.time() - start)



def palindrome_1(s: str) -> bool:
    '''
    1. s(str) 입력으로 받음
    2. 빈 리스트(strs) 생성
    3. isalnum() --> 영어/한글/숫자 중 하나면 True, 아니면 False 리턴
    4. strs.pop() --> 인자로 들어가는 위치의 리스트 값을 제거
                ex) strs.pop(0) --> 첫번째 인덱스의 리스트값 제거
                ex) strs.pop() --> 마지막 인덱스의 리스트값 제거
                선언과 동시에 수행이 된다
    5. 첫번째 위치와 마지막 위치 원소값을 계속 매치하면서 값을 제거
    '''
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True
            
start = time.time()
string = 'A man, a plan, a canal: Panama'
#string = 'race a car'
palindrome_1(string)
print(time.time() - start) 



def palindrome_2(s: str) -> bool:
    '''
    Deque형을 이용한 시간 최적화
    일반적으로 리스트를 많이 쓰게 되면 시간이 너무 오래 걸린다!
    리스트는 원소를 찾는데 모든 원소를 찾기 때문에...
    --> Deque 데이터형 사용(Deque는 딱 그 원소에 다이렉트로 간다)
    strs.popleft() 함수를 사용한게 차이
    --> pop 자체가 오른쪽부터 시작되어 왼쪽부터 수행하는 popleft() 사용
    '''
    strs: Deque = collections.deque()
    
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

start = time.time()
string = 'A man, a plan, a canal: Panama'
#string = 'race a car'
palindrome_2(string)
print(time.time() - start) 



def palindrome_3(s: str) -> bool:
    '''
    위에서 시도한 정규식->리스트 방법을 슬라이싱으로 더 빠르게 처리 가능
    s[::-1] 문자열을 반대로 뒤집는 기능
    '''
    s = s.lower()
    s = re.sub('^[a-zA-Z0-9]', '', s)
    
    return s == s[::-1]

start = time.time()
string = 'A man, a plan, a canal: Panama'
#string = 'race a car'
palindrome_3(string)
print(time.time() - start) 