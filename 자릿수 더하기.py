# 문제 설명
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 제한사항
# - N의 범위 : 100,000,000 이하의 자연수

def solution(n):
    if n >= 1 and n <= 100000000 :
        n = str(n)
        answer = sum([int(n[i]) for i in range(0,len(n))])
    else :
        answer = '잘못입력하였습니다'
    return answer

solution(123)
solution(987)
