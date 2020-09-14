Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def solution(n, m) :
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
