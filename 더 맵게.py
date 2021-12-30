# https://programmers.co.kr/learn/courses/30/lessons/42626

def solution(scoville, K):
    answer = 0
    while sum([0 if i >= K else 1 for i in scoville]) != 0:
        scoville = sorted(scoville)
        min1 = scoville.pop(0)
        min2 = scoville.pop(1)
    
        new = min1 + (min2 * 2)
        scoville.append(new)
        answer += 1
    
    return answer

solution([1, 2, 3, 9, 10, 12], 7)
