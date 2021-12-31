# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    num = [i for i in range(0, 10)]
    answer = sum(list(map(lambda x : x if x not in numbers else 0, num)))
    return answer

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))
