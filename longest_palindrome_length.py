'''
프로그래머스 level 3 :

문자열 s가 주어졌을때, s의 부분문자열 중 가장 긴 팰린드롬의 길이를 리턴하는 solution함수 작성
abcdcba --> 7  ,  abacde --> 3
'''

def solution(s):
    '''
    string이 주어진 경우, i, j 투 포인터가 돌면서 부분문자열(new_s) 생성
    i가 한칸 이동할수록 역순으로 이동하는 j의 범위는 줄어듦
    '''
    answer = 0
    
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            new_s = s[i:j]
            if new_s == new_s[::-1]:
                answer = max(answer, len(new_s))
    return answer

string = 'abcdcba'    
result = solution(string)
print(result)
