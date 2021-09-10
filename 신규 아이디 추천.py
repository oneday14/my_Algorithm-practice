# url : https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

def solution(new_id):
    new_id = new_id.lower()
    
    for i in new_id :
        if i.isalnum() :
            pass
        elif i in('-', '_', '.') :
            pass
        else :
            new_id = new_id.replace(i, '')
            
    for i in new_id :
        new_id = '.'.join([i for i in new_id.split('.') if i != '' ])
    
    if new_id != '' :
        
        while (new_id[-1] == '.') :        
            new_id = new_id.rstrip('.')
        
    else : 
        new_id = 'a'
        
    if len(new_id) >= 16 :
        new_id = new_id[0:15]
    
        while (new_id[-1] == '.') :        
            new_id = new_id.rstrip('.')
            
    elif len(new_id) <= 2 :
        while len(new_id) <= 2 :        
            new_id += new_id[-1]
    
    answer = new_id
    return answer

solution("...!@BaT#*..y.abcdefghijklm") == 'bat.y.abcdefghi'
solution("z-+.^.") == "z--"
solution("=.=") == "aaa"
solution("123_.def") == "123_.def"
solution("abcdefghijklmn.p") == 	"abcdefghijklmn"

