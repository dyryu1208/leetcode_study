import collections
import time
import re
from typing import List
'''
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자를 구분하지 않으며, 구두점(마침표, 쉼표 등) 역시 무시한다.

입력 : 
    paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
    banned = ['hit']

출력 : 
    'ball'
'''

def freq_word_dy(string, ban_word):
    '''
    inputs:
        string -> paragraph
        ban_word -> 금지어
    
    outputs:
        most_freq -> value값(등장횟수)이 가장 큰 딕셔너리의 key(단어)
    
    1) string.lower() & 정규표현식
    2) 금지어가 있으면 해당 단어 배제
    3) 단어별 등장횟수 체크(dict를 만들어 key에 단어, value에 등장횟수 저장)
    4) dict의 최대 value를 갖는 key 리턴
    '''
    string = re.sub(r'[^a-z0-9]',' ',string.lower())
    string = [word for word in string.split() if word not in ban_word]
    
    word_freq = {}
    for word in string:
        word_freq[word] = string.count(word)
        
    most_freq = max(word_freq, key=word_freq.get)
    return most_freq


def freq_word_1(paragraph: str, banned: List[str]) -> str:
    '''
    위 freq_word_dy에서 적은 1~2 과정을 한번에 words에 저장했음
    counts.most_common : 최빈 단어와 횟수를 가져오는 메서드
    다행히 시간차는 크게 나지 않는다
    * 많이 쓰이는 Counter 메서드
    from collections import defaultDict, combination, permutations, Counter
    '''
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split() if word not in banned]
    
    # counts의 결과 -> Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

start = time.time()    
ban_word = ['hit']
string = 'Bob hit a ball, the hit BALL flew far after it was hit.'

for iter in range(10):
    freq_word_1(string, ban_word)
    
print(time.time() - start)
print(freq_word_1(string, ban_word))
