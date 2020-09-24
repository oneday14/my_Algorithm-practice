# 문제 설명
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는
# 암호화 방식을 시저 암호라고 합니다. 예를 들어 “AB”는 1만큼 밀면 “BC”가 되고,
# 3만큼 밀면 “DE”가 됩니다. “z”는 1만큼 밀면 “a”가 됩니다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수,
# solution을 완성해 보세요.

# 제한 조건
# - 공백은 아무리 밀어도 공백입니다.
# - s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# - s의 길이는 8000이하입니다.
# - n은 1 이상, 25이하인 자연수입니다.

def solution(s, n) :
    upp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    low = list(map(lambda x : x.lower(), upp[0:26]))
    
    answer = ''
    for i in s :
        if i in upp : 
            for j in range(len(upp)) :
                if i == upp[j] :
                    answer = answer + upp[(j + n) % 26]
        elif i in low : 
            for j in range(len(low)) :
                if i == low[j] :
                    answer = answer + low[(j + n) % 26]
        else :
            answer = answer + ' '
    return answer

solution('AB', 1)
solution('z', 1)
solution('a B z', 4)
