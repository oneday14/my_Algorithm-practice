# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# - n은 0 이상 3000이하인 정수입니다.

def solution(n) :
    if n >= 0 and n <= 3000 :
        a1 = 0
        for i in range(1, n+1) :
            if n % i == 0 :
                a1 = a1 + i
            else :
                pass
            answer = a1
    else :
        answer = '잘못입력하였습니다'
    return answer

solution(12)
solution(5)
