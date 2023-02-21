import time
"""
가장 긴 팰린드롬 부분 문자열을 출력하라.

입력 : 
    'babad'
    'cbbd'

출력 : 
    'bab' 또는 'aba'
    'bb'
"""

def longest_pd_1(string: str) -> str:
    '''
    투 포인터가 좌측에서 우측으로 이동하고, 
    가장 긴 팰린드롬을 중앙을 중심으로 확장하며 탐색하는 형태
    '''
    
    def expand(left:int, right:int) -> str:
        while left>=0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        
        return string[left + 1:right]

    if len(string) < 2 or string == string[::-1]:
        return string

    result = ''
    for i in range(len(string)-1):
        result = max(result, 
                     expand(i, i+1),
                     expand(i, i+2),
                     key=len)
        
    return result

start = time.time()    
string = 'babad'

for iter in range(10):
    result = longest_pd_1(string)

print(time.time() - start)
print(result)
