#문장부호
punctuation_marks = [
    ".", "?", "!",
    ",", ";", ":"
]
punctuation_marks_braille = [
    [0,0,1,1,0,1], [0,0,1,0,1,1], [0,0,1,1,1,0],
    [0,0,1,0,0,0], [0,0,1,0,1,0], [0,0,1,1,0,0]
]


#숫자
num = ["1","2","3","4","5",
       "6","7","8","9","0"]
num_braille = [
    [1,0,0,0,0,0],[1,0,1,0,0,0],[1,1,0,0,0,0],[1,1,0,1,0,0],[1,0,0,1,0,0],
    [1,1,1,0,0,0],[1,1,1,1,0,0],[1,0,1,1,0,0],[0,1,1,0,0,0],[0,1,1,1,0,0]
]

#영어
# eng = ['A', 'B', 'C', 'D', 'E',
#        'F', 'G', 'H', 'I', 'J',
#        'K', 'L', 'M', 'N', 'O',
#        'P', 'Q', 'R', 'S', 'T',
#        'U', 'V', 'W', 'X', 'Y', 'Z']
eng = ['a', 'b', 'c', 'd', 'e',
       'f', 'g', 'h', 'i', 'j',
       'k', 'l', 'm', 'n', 'o',
       'p', 'q', 'r', 's', 't',
       'u', 'v', 'w', 'x', 'y', 'z']

eng_braille = [
        [1,0,0,0,0,0], [1,0,1,0,0,0], [1,1,0,0,0,0], [1,1,0,1,0,0], [1,0,0,1,0,0],
        [1,1,1,0,0,0], [1,1,1,1,0,0], [1,0,1,1,0,0], [0,1,1,0,0,0], [0,1,1,1,0,0],
        [1,0,0,0,1,0], [1,0,1,0,1,0], [1,1,0,0,1,0], [1,1,0,1,1,0], [1,0,0,1,1,0],
        [1,1,1,0,1,0], [1,1,1,1,1,0], [1,0,1,1,1,0], [0,1,1,0,1,0], [0,1,1,1,1,0],
        [1,0,0,0,1,1], [1,0,1,0,1,1], [0,1,1,1,0,1], [1,1,0,0,1,1], [1,1,0,1,1,1], [1,0,0,1,1,1]
]

def finish_sig(cnt,input,text): #대문자 종료 시그널
    if len(input)-1 > cnt :
        if [input[cnt],input[cnt+1]] == [[0,0,0,0,0,1],[0,0,0,0,1,0]]: # 대문자 종료표 확인
            return True,2
        if input[cnt] in punctuation_marks_braille:
            return True,0
    return False, 0

def make_upper(cnt,input,text):
    if input[cnt] in eng_braille:
        idx = eng_braille.index(input[cnt])
        text.append([eng[idx].upper(),0])
        return cnt+1,True,text

def check_upper(cnt,input,text):
    upper_sig_cnt = 0 # 대문자점자 신호 카운트
    while True:
        if input[cnt] == [0,0,0,0,0,1]:
            upper_sig_cnt += 1
            cnt += 1
        else:
            break

    if upper_sig_cnt == 0:
        return cnt, False,text
    elif upper_sig_cnt == 1:
        cnt, tmp, text = make_upper(cnt,input,text)
        return cnt,True,text
    elif upper_sig_cnt == 2:
        while True:
            finish,c = finish_sig(cnt, input, text)
            if finish:
                cnt += c
                break
            if len(input) == cnt or input[cnt] == " " or \
                    input[cnt] == [0,0,0,0,0,1] or input[cnt] == [0,1,0,1,1,1]: # 조건 더 추가해야함
                break
            cnt,tmp,text = make_upper(cnt,input,text)
        return cnt,True,text
    elif upper_sig_cnt == 3:
        while True:
            finish, c = finish_sig(cnt, input, text)
            if finish:
                cnt += c
                break
            if input[cnt] == " " :
                text.append([' ',0])
                cnt += 1
                continue
            cnt, tmp, text = make_upper(cnt, input, text)
        return cnt, True, text

def check_lower(cnt,input,text):
    if input[cnt] in eng_braille:
        idx = eng_braille.index(input[cnt])
        text.append([eng[idx],0])
        return cnt+1,True,text
    else:
        return cnt, False,text


def check_num(cnt,input,text) :
    if input[cnt] == [0,1,0,1,1,1]:
        while True:
            cnt += 1
            if cnt < len(input) and input[cnt] in num_braille:
                idx = num_braille.index(input[cnt])
                text.append([num[idx],0])
            else:
                break
        return cnt, True, text
    else:
        return cnt, False, text

def check_punctuation_marks(cnt,input,text):
    if input[cnt] in punctuation_marks_braille:
        idx = punctuation_marks_braille.index(input[cnt])
        text.append([punctuation_marks[idx],0])
        return cnt+1,True,text
    else:
        return cnt, False,text