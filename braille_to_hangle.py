"""
test
? = [[0,0,1,0,1,1]]  # 문장부호 오류가 발생 -> jamo라이브러리 오류라 나온다 -> 해결 못함.. -> 오류해결 
그래서  = [[1,0,0,0,0,0],[0,1,1,0,1,0] ]
구 = [[0,1,0,0,0,0],[1,1,0,0,1,0]]
걲 = [[0,1,0,0,0,0],[1,1,0,1,0,1],[1,0,0,0,0,0]]
실기 = [[0,0,0,0,0,1],[1,0,0,1,1,0],[0,0,1,0,0,0],[0,1,0,0,0,0],[1,0,0,1,1,0]]
까 = [[0,0,0,0,0,1],[1,1,1,0,0,1]]
억 = [[1,1,0,1,0,1]]
1 = [[1,0,0,0,0,0]]
ㅏ = [[1,0,1,0,0,1]]
아이 = [[1,0,1,0,0,1],[1,0,0,1,1,0]]
우유 = [[1,1,0,0,1,0],[1,1,0,0,0,1]]
중앙 = [[0,1,0,0,0,1],[1,1,0,0,1,0],[0,0,1,1,1,1],[1,0,1,0,0,1],[0,0,1,1,1,1]]
발음 = [[0,1,0,1,0,0],[0,0,1,0,0,0],[0,1,1,0,0,1],[0,0,1,0,0,1]]
솥뚜껑 = [[0,0,0,0,0,1],[1,0,0,0,1,1],[0,0,1,0,1,1],[0,0,0,0,0,1],[0,1,1,0,0,0],[1,1,0,0,1,0],[0,0,0,0,0,1],[0,1,0,0,0,0],[0,1,1,0,1,0],[0,0,1,1,1,1]]
소뼈 = [[0,0,0,0,0,1],[1,0,0,0,1,1],[0,0,0,0,0,1],[0,1,0,1,0,0],[1,0,0,1,0,1]]
국어 = [[0,1,0,0,0,0],[1,1,0,0,1,0],[1,0,0,0,0,0],[0,1,1,0,1,0]]
낚시 = [[1,1,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,1],[1,0,0,1,1,0]]
있다 = [[1,0,0,1,1,0],[0,1,0,0,1,0],[0,1,1,0,0,0]]
삯 = [[1,0,1,0,1,0],[1,0,0,0,0,0],[0,0,0,0,1,0]]
앉다 = [[1,0,1,0,0,1],[0,0,1,1,0,0],[1,0,0,0,1,0],[0,1,1,0,0,0]]
얘기 = [[0,1,0,1,1,0],[1,0,1,1,1,0],[0,1,0,0,0,0],[1,0,0,1,1,0]]
"""
from braille_to_hangle_funtion import *
from read_pdf import Pdf_to_braille # from 옆에 read_pdf.py 파일 위치로 변경해서 사용하세요

def join_text(text):
    t = []
    for T,N in text:
        t.append(T)
    return join_jamos(t)

def add_output(end_char, text):
    output = join_text(text) + end_char
    text = []
    return output,text


# input = [[1, 1, 0, 1, 0, 0],[0, 1, 0, 0, 1, 0]] #폐 o
# input = [[1, 1, 0, 1, 0, 0],[1, 0, 1, 0, 0, 1],[0, 1, 0, 0, 1, 0]] #팠 x 파+예
# input = [[0, 1, 0, 0, 1, 0]] #예 o
# input = [[1, 0, 1, 0, 0, 1],[0, 1, 0, 0, 1, 0]] #았 x 아+예
# input = [[1, 1, 0, 0, 0, 0],[0, 1, 0, 0, 1, 0],[0, 1, 0, 0, 1, 0]] #녰x 녜+예
# input = [[1, 1, 0, 0, 0, 0],[0, 1, 0, 0, 1, 0]] # 났 o / 녜 x
#제일 최근에 주석 처리한 것
#input = [[1, 0, 1, 0, 0, 1],[0, 0, 1, 1, 0, 0],[1, 1, 0, 0, 0, 0],[1, 1, 1, 1, 0, 1],[0, 1, 0, 1, 1, 1],[1, 0, 0, 0, 0, 0],[1, 0, 1, 0, 0, 0],[1, 1, 0, 0, 0, 0],[0, 1, 0, 1, 0, 0],[0, 1, 0, 1, 0, 0],[1, 1, 0, 0, 1, 0]]



def brailleRun():
    input = Pdf_to_braille('점자.pdf')[0]
    cnt = 0
    output = []
    text = []
    while True:
        if cnt == len(input): # while문 종료 조건
            tmp, text = add_output("", text)
            output += tmp
            break

        if input[cnt] == " ": # 띄어쓰기 시 text에 있는 내용을 output에 저장
            tmp,text = add_output(" ",text)
            output += tmp
            cnt += 1
            continue

        if input[cnt] == "\n": # 엔터 시 text에 있는 내용을 output에 저장
            tmp,text = add_output("<br>",text)
            output += tmp
            cnt += 1
            continue


        #숫자
        cnt, tmp, text = check_num(cnt, input, text)
        if tmp == True: continue

        #부사
        cnt, tmp, text = check_adverb(cnt, input, text)
        if tmp == True: continue

        #약어
        cnt,tmp,text = check_acronyms1(cnt, input, text)
        if tmp == True: continue
        cnt,tmp,text = check_acronyms2(cnt,input,text)
        if tmp == True : continue

        #초성
        cnt,tmp,text = check_chosung(cnt,input,text)
        if tmp == True : continue

        #중성
        cnt,tmp,text = check_jungsung(cnt,input,text)
        if tmp == True : continue

        #종성
        cnt,tmp,text = check_jongsung(cnt,input,text)
        if tmp == True: continue
    print("이게 output원본")
    print(output)
    s = "".join(output)
    print(s)

    return s

Tinput = 'a'

def T_Hangle_brailleRun():
    cnt = 0
    output = []
    text = []
    while True:
        if cnt == len(Tinput): # while문 종료 조건
            tmp, text = add_output("", text)
            output += tmp
            break

        if Tinput[cnt] == " ": # 띄어쓰기 시 text에 있는 내용을 output에 저장
            tmp,text = add_output(" ",text)
            output += tmp
            cnt += 1
            continue

        if Tinput[cnt] == "\n": # 엔터 시 text에 있는 내용을 output에 저장
            tmp,text = add_output("\n",text)
            output += tmp
            cnt += 1
            continue

        #숫자
        cnt, tmp, text = check_num(cnt, Tinput, text)
        if tmp == True: continue

        #부사
        cnt, tmp, text = check_adverb(cnt, Tinput, text)
        if tmp == True: continue

        #약어
        cnt,tmp,text = check_acronyms1(cnt, Tinput, text)
        if tmp == True: continue
        cnt,tmp,text = check_acronyms2(cnt,Tinput,text)
        if tmp == True : continue

        #초성
        cnt,tmp,text = check_chosung(cnt,Tinput,text)
        if tmp == True : continue

        #중성
        cnt,tmp,text = check_jungsung(cnt,Tinput,text)
        if tmp == True : continue

        #종성
        cnt,tmp,text = check_jongsung(cnt,input,text)
        if tmp == True: continue
    print(output)
    print(output)
    s = "".join(output)
    print(s)

    return s























