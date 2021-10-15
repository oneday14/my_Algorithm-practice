# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    split_str = [int(i) for i in s.split(' ')]
    answer = str(min(split_str)) + ' ' + str(max(split_str))
    return answer

solution("1 2 3 4")
solution("-1 -2 -3 -4")
solution("-1 -1")
