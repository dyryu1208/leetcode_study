import time
from typing import List
'''
로그를 재정렬하라. 기준은 다음과 같다
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않으나, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

입력 : logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
출력 : ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]


문자로 구성된 로그 let1, let2, let3이 dig1, dig2보다 앞에 와야
-> 문자로그는 뒤 <art can>, <art zero> , <own kit dig>의 순서로 정렬?
   + 문자가 동일할 경우 식별자 순
-> 숫자로그는 입력순서대로
'''

def log_sorting_dy(logs):
    '''
    1. 문자로그 앞으로 땡김
    2. 알파벳 순으로 정렬
    3. 문자가 전부 동일한 경우 식별자 순으로 정렬
    4. 숫자로그 입력 순서대로
    
    -> 숫자로 시작하는 놈들은 log_num에, 문자로 시작하는 놈들은 log_char에 append
    -> 자동적으로 log_num은 들어온 순서로 정렬될 것
    -> log_char은 알파벳 순으로 정렬
    '''
    
    log_char = []
    log_num = []
    
    for element in logs:
        if element.split()[1].isalpha():
            log_char.append(element)
        else:
            log_num.append(element)
    
    # sort를 해야될 것 같은데 어떻게 해야 될지 모르겠음
    # https://sennieworld.tistory.com/46
    log_char = sorted(log_char, key=lambda x: x.split()[1:])
    return log_char + log_num
    
start = time.time()

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
logs_2 = log_sorting_dy(logs)
print(logs_2)

print(time.time() - start)



def log_sorting_1(logs: List[str]) -> List[str]:
    
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    
    return letters + digits

start = time.time()

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
logs_2 = log_sorting_1(logs)
print(logs_2)

print(time.time() - start)