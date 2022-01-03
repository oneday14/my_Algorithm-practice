# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    num = [i for i in range(2, n)]

    for i in num:
        if n % i == 1:
            answer = i
            break
    
    return answer

print(solution(10))	    # 3
print(solution(12))	    # 11
