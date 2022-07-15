# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    dict_name = {}  # 신고 dict
    dict_cnt = {}   # 신고 당한 횟수 dict
    dict_mail = {}  # 메일 수 dict
    for id_name in id_list:
        dict_name[id_name] = []
        dict_cnt[id_name] = 0
        dict_mail[id_name] = 0
        
    reports = set(report)
    
    for pair in reports:
        from_name = pair.split(" ")[0]
        to_name = pair.split(" ")[1]
        
        dict_name[from_name].append(to_name)
        dict_cnt[to_name] += 1
        
    print(dict_name)
    print(dict_cnt)
    
    warnings = [pair[0] for pair in dict_cnt.items() if pair[1] >= k]
    print(warnings)

    for name in warnings:
        for pair in dict_name.items():
            if name in pair[1]:
                dict_mail[pair[0]] += 1
    
    answer = list(dict_mail.values())
    
    return answer


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2) # [2,1,1,0]
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3 # [0,0]
