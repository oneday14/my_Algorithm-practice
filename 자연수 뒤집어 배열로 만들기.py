# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

def solution(n):
    n = str(n)
    answer = []
    for i in range(len(n)-1,-1,-1) :
        answer.append(int(n[i]))
    return answer

solution(12345)
