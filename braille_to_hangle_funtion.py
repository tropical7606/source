#숫자
num = ["1","2","3","4","5",
       "6","7","8","9","0"]
num_braille = [
    [1,0,0,0,0,0],[1,0,1,0,0,0],[1,1,0,0,0,0],[1,1,0,1,0,0],[1,0,0,1,0,0],
    [1,1,1,0,0,0],[1,1,1,1,0,0],[1,0,1,1,0,0],[0,1,1,0,0,0],[0,1,1,1,0,0]
]

#초성
chosung = [
    "ㄱ","ㄴ","ㄷ","ㄹ","ㅁ",
    "ㅂ","ㅅ","ㅈ","ㅊ",
    "ㅋ","ㅌ","ㅍ","ㅎ"]
chosung_braille = [
    [0,1,0,0,0,0], [1,1,0,0,0,0], [0,1,1,0,0,0], [0,0,0,1,0,0], [1,0,0,1,0,0],
    [0,1,0,1,0,0], [0,0,0,0,0,1], [0,1,0,0,0,1], [0,0,0,1,0,1],
    [1,1,1,0,0,0], [1,0,1,1,0,0], [1,1,0,1,0,0], [0,1,1,1,0,0]
]

#종성
jongsung = [
    "ㄱ","ㄴ","ㄷ","ㄹ","ㅁ",
    "ㅂ","ㅅ","ㅇ","ㅈ","ㅊ",
    "ㅋ","ㅌ","ㅍ","ㅎ","ㅆ"]
jongsung_braille = [
    [1,0,0,0,0,0],[0,0,1,1,0,0],[0,0,0,1,1,0],[0,0,1,0,0,0],[0,0,1,0,0,1],
    [1,0,1,0,0,0],[0,0,0,0,1,0],[0,0,1,1,1,1],[1,0,0,0,1,0],[0,0,1,0,1,0],
    [0,0,1,1,1,0],[0,0,1,0,1,1],[0,0,1,1,0,1],[0,0,0,1,1,1],[0,1,0,0,1,0]
]

#겹받침
key_gyeobbadchim = ["ㄲ", "ㄳ", "ㄵ", "ㄶ", "ㄺ", "ㄻ",
                    "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅄ"]
value_gyeobbadchim = [['ㄱ','ㄱ'], ['ㄱ','ㅅ'], ['ㄴ','ㅈ'], ['ㄴ','ㅎ'], ['ㄹ','ㄱ'], ['ㄹ','ㅁ'],
                      ['ㄹ','ㅂ'], ['ㄹ','ㅅ'], ['ㄹ','ㅌ'], ['ㄹ','ㅍ'], ['ㄹ','ㅎ'], ['ㅂ','ㅅ']]
gyeobbadchim = dict()  #겹받침들을 딕셔너리 형대로 만든것 ex key: ㄲ , value: ['ㄱ','ㄱ']
for i in range(len(key_gyeobbadchim)):
    gyeobbadchim[key_gyeobbadchim[i]] = value_gyeobbadchim[i]

#중성
jungsung = [
    "ㅏ","ㅑ","ㅓ","ㅕ","ㅗ",
    "ㅛ","ㅜ","ㅠ","ㅡ","ㅣ",
    "ㅐ","ㅔ","ㅚ","ㅘ","ㅝ",
    "ㅢ","ㅖ"
    ]
jungsung_braille = [
    [1,0,1,0,0,1],[0,1,0,1,1,0],[0,1,1,0,1,0],[1,0,0,1,0,1],[1,0,0,0,1,1],
    [0,1,0,0,1,1],[1,1,0,0,1,0],[1,1,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,1,0],
    [1,0,1,1,1,0],[1,1,0,1,1,0],[1,1,0,1,1,1],[1,0,1,0,1,1],[1,1,1,0,1,0],
    [0,1,1,1,0,1],[0,1,0,0,1,0]
]
jungsung2 = [
    "ㅒ", "ㅙ", "ㅞ", "ㅟ"
]
jungsung_braille2=[
    [[0,1,0,1,1,0],[1,0,1,1,1,0]], [[1,0,1,0,1,1],[1,0,1,1,1,0]], [[1,1,1,0,1,0],[1,0,1,1,1,0]], [[1,1,0,0,1,0],[1,0,1,1,1,0]]
]

from unicode import join_jamos,split_syllables # from 옆에 read_pdf.py 파일 위치로 변경해서 사용하세요
def make_gyeobbadchim(a,b): #겹받침 만드는 함수 -> 함수명 좋은거 있음 바꿔주세요...
    #"ㄲ" "ㄳ", "ㄵ", "ㄶ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅄ"
    g_keys = list(gyeobbadchim.keys())
    g_values = list(gyeobbadchim.values())
    position = g_values.index([a,b])
    return g_keys[position]


# 약자
acronyms_1 = ['가','나','다','마','바','사',
              '자','카','타','파','하']
acronyms_1_braille = [
    [1,1,1,0,0,1],[1,1,0,0,0,0],[0,1,1,0,0,0],[1,0,0,1,0,0],[0,1,0,1,0,0],[1,0,1,0,1,0],
    [0,1,0,0,0,1],[1,1,1,0,0,0],[1,0,1,1,0,0],[1,1,0,1,0,0],[0,1,1,1,0,0]
]

acronyms_2 = ['억', '언', '얼', '연', '열', '영', '옥',
              '온', '옹', '운', '울', '은', '을', '인']
acronyms_2_braille = [
    [1,1,0,1,0,1],[0,1,1,1,1,1],[0,1,1,1,1,0],[1,0,0,0,0,1],[1,0,1,1,0,1],[1,1,1,1,0,1],[1,1,0,0,1,1],
    [1,0,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,0,0],[1,1,1,0,1,1],[1,0,0,1,1,1],[0,1,1,0,1,1],[1,1,1,1,1,0]
]
# 부사
adverb = ['그래서', '그러나', '그러면',
          '그러므로', '그런데', '그리고','그리하여']
adverb_braille = [[[1,0,0,0,0,0],[0,1,1,0,1,0]], [[1,0,0,0,0,0],[1,1,0,0,0,0]], [[1,0,0,0,0,0],[0,0,1,1,0,0]],
                  [[1,0,0,0,0,0],[0,0,1,0,0,1]], [[1,0,0,0,0,0],[1,1,0,1,1,0]], [[1,0,0,0,0,0],[1,0,0,0,1,1]], [[1,0,0,0,0,0],[1,0,0,1,0,1]]]

def check_adverb(cnt,input,text):

    if len(text) == 0 and cnt < len(input) - 1 and [input[cnt], input[cnt + 1]] in adverb_braille:
        idx = adverb_braille.index([input[cnt], input[cnt + 1]])
        text.append([adverb[idx], 0])
        return cnt + 2, True, text
    else:
        return cnt,False,text

def check_acronyms1(cnt,input,text):
    # 까,싸는 된소리[0,0,0,0,0,1] + 가,사 = 까,싸
    if input[cnt] == [0,0,0,0,0,1]:
        if input[cnt+1] in [acronyms_1_braille[0],acronyms_1_braille[5]]:
            idx = acronyms_1_braille.index(input[cnt+1])
            cho, jong = split_syllables(acronyms_1[idx])
            text.append([make_pair_jaeum(cho), 1])
            text.append([jong, 2])
            return cnt + 2, True, text

    elif input[cnt] in acronyms_1_braille:
        # 가,사만 약자가 따로 있고
        # 나머지 나,다,마,바,자,카,타,파,하는 약자가 각자음의 초성과 같아서
        # 나,다,마,바,자,카,타,파,하 뒤에 초성과 종성이 있는지 판단하여
        # 둘중 하나라도 있으면 'ㅏ'를 붙여준다
        if cnt < len(input)-1 and (input[cnt] != acronyms_1_braille[0] and input[cnt] != acronyms_1_braille[5]):
            tmp_text = text.copy()
            _, tmp1,_ = check_chosung(cnt + 1, input, text)
            text = tmp_text

            # tmp_text = text.copy()
            # _, tmp2, _ = check_jongsung(cnt + 1, input, text)
            # text = tmp_text
            ################################################# 이부분 고쳐야함 삼한사온 종성ㅁ+종성ㄴ
            tmp2 = False
            if input[cnt+1] in jongsung_braille[:-1]:
                tmp2 = True
            #################################################
            if tmp2 == False and tmp1 == False and input[cnt+1] != ' ':
                return cnt, False, text

        idx = acronyms_1_braille.index(input[cnt])
        cho, jong = split_syllables(acronyms_1[idx])
        text.append([cho,1])
        text.append([jong,2])
        return cnt + 1, True, text
    else:
        return cnt,False,text

    return cnt, False, text


def check_acronyms2(cnt,input,text):
    # 껏는 된소리[0,0,0,0,0,1] + 것 = 껏
    if input[cnt] == [0, 0, 0, 0, 0, 1]:
        if cnt+1 < len(input) - 1 and [input[cnt+1], input[cnt+2]] == [[0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0]]:
            text.append([make_pair_jaeum('ㄱ'), 1])
            text.append(['ㅓ', 2])
            text.append(['ㅅ', 3])
            return cnt + 3, True, text

    # 약자 - 것 [[0,1,0,1,0,1],[0,1,1,0,1,0]] 체크
    if cnt < len(input) - 1 and [input[cnt], input[cnt + 1]] == [[0,1,0,1,0,1],[0,1,1,0,1,0]]:
        text.append(['ㄱ', 1])
        text.append(['ㅓ', 2])
        text.append(['ㅅ', 3])
        return cnt + 2, True, text
    elif input[cnt] in acronyms_2_braille:

        idx = acronyms_2_braille.index(input[cnt])
        cho,jong,jung = split_syllables(acronyms_2[idx])

        # 성,썽,정,쩡,청 은 예외적으로 엉을 나타낼때 영의 약자를 사용
        if len(text) != 0 and input[cnt] == [1,1,1,1,0,1] \
                and text[-1][1] == 1 and text[-1][0] in ['ㅅ', 'ㅆ', 'ㅈ', 'ㅉ', 'ㅊ']:
            text.append(['ㅓ', 2])
            text.append([jung, 3])
            return cnt + 1, True, text
        if len(text) == 0 or (len(text) != 0 and text[-1][1] != 1):
            text.append([cho,1])
        text.append([jong,2])
        text.append([jung,3])
        return cnt+1,True,text
    else:
        return cnt,False,text



def make_pair_jaeum(jaeum):
    if jaeum == 'ㄱ':
        return ("ㄲ")
    elif jaeum == 'ㄷ':
        return ("ㄸ")
    elif jaeum == 'ㅂ':
        return ("ㅃ")
    elif jaeum == 'ㅅ':
        return ("ㅆ")
    elif jaeum == 'ㅈ':
        return ("ㅉ")


def check_chosung(cnt,input,text): # 초성 판단
    if input[cnt] in chosung_braille:
        idx = chosung_braille.index(input[cnt])

        # 된소리 확인
        if len(text) != 0 and text[-1][1] == 1 and text[-1][0]=='ㅅ':
            text[-1][0] = make_pair_jaeum(chosung[idx])
            return cnt+1,True, text

        text.append([chosung[idx],1])
        return cnt+1,True,text
    else:
        return cnt,False,text


def check_jungsung(cnt,input,text): #중성
    if cnt < len(input) - 1 and [input[cnt],input[cnt+1]] in jungsung_braille2:
        idx = jungsung_braille2.index([input[cnt],input[cnt+1]])
        # 첫소리에 자음 없이 모음만 올 경우, 모음 앞에 ㅇ 추가 (ex.ㅏ -> 아)
        if len(text) == 0 or (len(text) != 0 and text[-1][1] != 1):
            text.append(['ㅇ', 1])

        text.append([jungsung2[idx], 2])
        return cnt+2, True, text

    if input[cnt] in jungsung_braille:
        idx = jungsung_braille.index(input[cnt])

        # 첫소리에 자음 없이 모음만 올 경우, 모음 앞에 ㅇ 추가 (ex.ㅏ -> 아)
        if len(text) == 0 or (len(text) != 0 and text[-1][1] != 1):
            text.append(['ㅇ', 1])

        # 중성 추가
        text.append([jungsung[idx], 2])

        # ㅖ의 점자와 ㅆ의 점자가 같아 구별하기 위한 부분
        if cnt < len(input)-1 and input[cnt+1] == [0, 1, 0, 0, 1, 0]:
            text.append(["ㅆ", 3])
            return cnt + 2, True, text

        if text[-2][0] != 'ㅇ' and text[-2][0] != 'ㅍ' and input[cnt] == [0, 1, 0, 0, 1, 0]:
            text[-1][0] = 'ㅏ'
            text.append(["ㅆ", 3])

        return cnt+1,True,text
    else:
        return cnt,False,text

def check_Doublesiot_Ye(cnt,input,text):
    if input[cnt] == [0, 1, 0, 0, 1, 0]:
        text.append(["ㅆ",2])
        return cnt+1,True,text
    else:
        return cnt,False,text

def check_jongsung(cnt,input,text): # 종성
    if input[cnt] in jongsung_braille:
        idx = jongsung_braille.index(input[cnt])

        #쌍받침
        if len(text) > 0 and text[-1][1] == 3:
            text[-1][0] = make_gyeobbadchim(text[-1][0],jongsung[idx])
            return cnt+1,True,text

        text.append([jongsung[idx], 3])
        return cnt+1,True,text
    else:
        return cnt,False,text


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








