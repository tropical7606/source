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
adverb = ['그래서', '그러나', '그러면', '그러므로', '그런데', '그리고']
adverb_braille = [[0,1,1,0,1,0], [1,1,0,0,0,0], [0,0,1,1,0,0], [0,0,1,0,0,1], [1,0,0,0,1,1]]

#겹받침
key_gyeobbadchim = ["ㄲ", "ㄳ", "ㄵ", "ㄶ", "ㄺ", "ㄻ",
                    "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅄ"]
value_gyeobbadchim = [['ㄱ','ㄱ'], ['ㄱ','ㅅ'], ['ㄴ','ㅈ'], ['ㄴ','ㅎ'], ['ㄹ','ㄱ'], ['ㄹ','ㅁ'],
                      ['ㄹ','ㅂ'], ['ㄹ','ㅅ'], ['ㄹ','ㅌ'], ['ㄹ','ㅍ'], ['ㄹ','ㅎ'], ['ㅂ','ㅅ']]
gyeobbadchim = dict()  #겹받침들을 딕셔너리 형대로 만든것 ex key: ㄲ , value: ['ㄱ','ㄱ']
for i in range(len(key_gyeobbadchim)):
    gyeobbadchim[key_gyeobbadchim[i]] = value_gyeobbadchim[i]


#문장부호
#가장 많이 쓰는 . ? ! , ~만 일단 함
sentenceSign  = ["~", ".", "!" , ",","?","-"]
sentenceSign_braille = [[[0,0,0,0,1,1],[0,0,0,0,1,1]],[0,0,1,1,0,1],[0,0,1,1,1,0],[0,0,0,1,0,0],[0,0,1,0,1,1],[0,0,0,0,1,1]]

#숫자
number = ["1","2","3","4","5","6","7","8","9","0"]
number_braille=[[1,0,0,0,0,0],[1,0,1,0,0,0],[1,1,0,0,0,0],[1,1,0,1,0,0],[1,0,0,1,0,0],
              [1,1,1,0,0,0],[1,1,1,1,0,0],[1,0,1,1,0,0],[0,1,1,0,0,0],[0,1,1,1,0,0]]
"""
자음 종성의 ㄱ과 1의 점자가 같다
이와 같이 같은 형태가 있으므로 다음 글자가 모음이라면 숫자가 아니라고 판단할 수 있도록 해준다
"""
#유리 추가 -> 문장부호, 숫자 (간단한 결과값 도출이므로 연산/ 영어 제외)

"""
test
? = [[0,0,1,0,1,1]]  # 문장부호 오류가 발생 -> jamo라이브러리 오류라 나온다 -> 해결 못함..
그래서  = [[1,0,0,0,0,0],[0,1,1,0,1,0] ]
구 = [[0,1,0,0,0,0],[1,1,0,0,1,0]]
걲 = [[0,1,0,0,0,0],[1,1,0,1,0,1],[1,0,0,0,0,0]]
실기 = [[0,0,0,0,0,1],[1,0,0,1,1,0],[0,0,1,0,0,0],[0,1,0,0,0,0],[1,0,0,1,1,0]]
까 = [[0,0,0,0,0,1],[1,1,1,0,0,1]]
억 = [[1,1,0,1,0,1]]
1 = [[1,0,0,0,0,0]]
ㅏ = [[1,0,1,0,0,1]]
 """

input = [[0,0,1,0,1,1]]
output = []


from hangul_utils import join_jamos,split_syllables

def make_gyeobbadchim(a,b): #겹받침 만드는 함수 -> 함수명 좋은거 있음 바꿔주세요...
    #"ㄲ" "ㄳ", "ㄵ", "ㄶ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅄ"
    g_keys = list(gyeobbadchim.keys())
    g_values = list(gyeobbadchim.values())
    position = g_values.index([a,b])
    return g_keys[position]

cnt = 0
text = []
while True:
    if cnt == len(input): # while문 종료 조건
        output.append(join_jamos(text)) # text에 저장된 자음모음을 합치는 작업
        break


    if input[cnt] == " ": #띄어쓰기
        text.append(" ")
        cnt += 1

    elif input[cnt] == [0,1,0,1,0,1]: # 것
        if input[cnt+1] == [0,1,1,0,1,0]:
            text.append("것")
            cnt += 2



    elif input[cnt] in number_braille:  # 숫자인지 확인하는 if문 -> 숫자와 자음의 점자가 같은 것도 있으므로 input[cnt +1 ]이 모음이라면 숫자가 아니라고 판단
        idx = number_braille.index(input[cnt])
        text.append(number[idx])
        cnt += 1

    #숫자인지 먼저 확인하고 부사인지 확인해야 숫자 결과값 알 수 있다
    elif (input[cnt] == [1,0,0,0,0,0]) and input[cnt+1] in adverb_braille: # 부사 '그래서', '그러나', '그러면', '그러므로', '그런데', '그리고'
        #다음에 글자가 있을 경우라고 명시 해줘야 함
        #즉 부사는 [1,0,0,0,0,0][~]로 이루어져 있으므로 현재 값이 [1,0,0,0,0,0]이면서 adverb_braille에 값이 있다면 부사로 본다(elif 조건에 대한 것)
        idx = adverb_braille.index(input[cnt+1]) #부사인 것을 알았으니 다음(cnt +1)을 통해 어떤 부사인지 확인한다
        text.append(adverb[idx])
        cnt += 2

    elif input[cnt] in acronyms_1_braille: # 약어1 '가','나','다','마','바','사','자','카','타','파','하'
        idx = acronyms_1_braille.index(input[cnt])
        text += list(split_syllables(acronyms_1[idx])) # ex) 가 -> ['ㄱ', 'ㅏ'] 자음분리(split_syllables함수 이용)를 한 다음 text에 추가
        cnt += 1

    elif input[cnt] in acronyms_2_braille: # 약어2 '억', '언', '얼', '연', '열', '영', '옥', '온', '옹', '운', '울', '은', '을', '인'
        idx = acronyms_2_braille.index(input[cnt])
        temp_text = list(split_syllables(acronyms_2[idx])) # ex) 억 -> ['ㅇ','ㅓ','ㄱ'] 자모분리

        # 약어2 앞에 초성 자음이 있는 확인 하는 if 문
        # [0,0,0,0,0,1]는 된소리 시작 표시 확인
        if (cnt != 0 and input[cnt-1] in chosung_braille) or (cnt > 1 and input[cnt-2] == [0,0,0,0,0,1]):
            temp_text.pop(0) # 자음'ㅇ' pop

        #종성 겹받침인지 확인하는 if문
        if cnt < len(input)-1 and input[cnt+1] in jongsung_braille:
            idx = jongsung_braille.index(input[cnt+1])
            g = make_gyeobbadchim(temp_text[-1], jongsung[idx]) #두자음을 겹침으로 만드는 함수 ex) 'ㄱ','ㄱ' -> 'ㄲ'
            temp_text.pop()
            temp_text.append(g)
            cnt += 1

        text += temp_text
        cnt += 1

    elif (input[cnt] == [0,0,0,0,0,1] and input[cnt+1] in chosung_braille)\
            or (input[cnt] == [0,0,0,0,0,1] and input[cnt+1] in acronyms_1_braille): # 된소리

        if input[cnt+1] == [0,1,0,0,0,0]:
            text.append("ㄲ")
        elif input[cnt+1] == [0,1,1,0,0,0]:
            text.append("ㄸ")
        elif input[cnt+1] == [0,1,0,1,0,0]:
            text.append("ㅃ")
        elif input[cnt+1] == [0,0,0,0,0,1]:
            text.append("ㅆ")
        elif input[cnt+1] == [0,1,0,0,0,1]:
            text.append("ㅉ")

        elif input[cnt+1] in acronyms_1_braille: #된소리 + 가 -> 까
            idx = acronyms_1_braille.index(input[cnt+1])
            a = acronyms_1[idx]
            if a == '가':
                a = '까'
            elif a == '다':
                a = '따'
            elif a == '바':
                a = '빠'
            elif a == '사':
                a = '싸'
            elif a == '자':
                a = '짜'

            text += list(split_syllables(a))  # ex) 가 -> ['ㄱ', 'ㅏ'] 자음분리

        cnt += 2

    elif input[cnt] in chosung_braille: # 초성
        idx = chosung_braille.index(input[cnt])
        text.append(chosung[idx])
        cnt += 1

    elif input[cnt] in jungsung_braille: # 중성
        idx = jungsung_braille.index(input[cnt])

        if cnt < len(input)-1 and input[cnt+1] == [1,0,1,1,1,0]: # ㅟ, ㅒ, ㅙ, ㅞ
            if input[cnt] == [1,1,0,0,1,0]:
                text.append("ㅟ")
            elif input[cnt] == [0,1,0,1,1,0]:
                text.append("ㅒ")
            elif input[cnt] == [1,0,1,0,1,1]:
                text.append("ㅙ")
            elif input[cnt] == [1,1,1,0,1,0]:
                text.append("ㅞ")
            cnt += 1

        else:
            if (cnt - 1) < 0:
                text.append("ㅇ")

            text.append( jungsung[idx])

        cnt += 1

    elif input[cnt] in sentenceSign_braille:  # 문장 부호
        idx = sentenceSign_braille.index(input[cnt])
        text.append(idx)
        cnt += 1

    elif input[cnt] in jongsung_braille: # 종성
        idx = jongsung_braille.index(input[cnt])
        j = jongsung[idx]

        if input[cnt-1] in jongsung_braille: # 겹받침이 되는지 확인하는 if문
            j = make_gyeobbadchim(text[-1], j)
            text.pop()

        text.append(j)
        cnt += 1









print("".join(output))


