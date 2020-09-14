# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# - 두 수는 1이상 1000000이하의 자연수입니다.

def solution(n, m) :
    if n >= 1 and n <= 1000000 and m >= 1 and m <= 1000000 :
        n_den = [i for i in range(1, n+1) if n % i == 0] 
        comm_den = [j for j in n_den if m % j == 0]
        answer = []
        answer.append(max(comm_den))
        lea_comm_mul = int((n * m) / max(comm_den))
        answer.append(lea_comm_mul)
    else :
        answer = '잘못입력하였습니다'
    return answer

solution(3,12)
solution(1,10)
