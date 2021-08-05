# tika 라이브러리를 이용한 점자 추출
"""
from tika import parser

pdf_path = "test.pdf"

# PDF 파일에서 텍스트를 추출
raw_pdf = parser.from_file(pdf_path)
contents = raw_pdf['content']
contents = contents.strip()

print(contents)
"""

# pdfminer 라이브러리를 이용한 점자 추출
import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

# PDF에서 점자 아스키코드로 뽑아오는 함수
def Pdf_to_ASCII(path):

    fp = open(path, 'rb') # PDF 오픈
    total_pages = PyPDF2.PdfFileReader(fp).numPages # PDF 페이지 수

    page_text = {} # PDF에서 읽어온 아스키값을 딕셔너리 형대로 저장한곳. 저장형식은 {페이지번호(0 ~ 페이지수-1) : 아스키코드값}
    for page_no in range(total_pages):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO() # PDF에서 읽어온 아스키코드 값이 있는곳.
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open(path, 'rb')
        password = ""
        maxpages = 0
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        caching = True
        pagenos = [page_no]

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
            interpreter.process_page(page)

        page_text[page_no] = retstr.getvalue() # 페이지번호(키)-출력값(값) 형태로 딕셔너리에 저장
        page_text[page_no] = page_text[page_no][:-1] # 이렇게 안해주면 출력했을때 맨뒤에 이상한 문자가 생겨서 해줌
    fp.close()
    device.close()
    retstr.close()


    return total_pages, page_text


def Pdf_to_braille(path):
    braille_ascii_dic = { # 아스키코드(키)-점자(값) 딕셔너리
        '!': [0, 1, 1, 0, 1, 1], '"': [0, 0, 0, 1, 0, 0], '#': [0, 1, 0, 1, 1, 1],
        '$': [1, 1, 1, 0, 0, 1], '%': [1, 1, 0, 0, 0, 1], '&': [1, 1, 1, 0, 1, 1],
        "'": [0, 0, 0, 0, 1, 0], '(': [1, 0, 1, 1, 1, 1], ')': [0, 1, 1, 1, 1, 1],
        '*': [1, 0, 0, 0, 0, 1], '+': [0, 1, 0, 0, 1, 1], ',': [0, 0, 0, 0, 0, 1],
        '-': [0, 0, 0, 0, 1, 1], '.': [0, 1, 0, 0, 0, 1], '/': [0, 1, 0, 0, 1, 0],
        '0': [0, 0, 0, 1, 1, 1], '1': [0, 0, 1, 0, 0, 0], '2': [0, 0, 1, 0, 1, 0],
        '3': [0, 0, 1, 1, 0, 0], '4': [0, 0, 1, 1, 0, 1], '5': [0, 0, 1, 0, 0, 1],
        '6': [0, 0, 1, 1, 1, 0], '7': [0, 0, 1, 1, 1, 1], '8': [0, 0, 1, 0, 1, 1],
        '9': [0, 0, 0, 1, 1, 0], ':': [1, 0, 0, 1, 0, 1], ';': [0, 0, 0, 1, 0, 1],
        '<': [1, 0, 1, 0, 0, 1], '=': [1, 1, 1, 1, 1, 1], '>': [0, 1, 0, 1, 1, 0],
        '?': [1, 1, 0, 1, 0, 1], '@': [0, 1, 0, 0, 0, 0], 'A': [1, 0, 0, 0, 0, 0],
        'B': [1, 0, 1, 0, 0, 0], 'C': [1, 1, 0, 0, 0, 0], 'D': [1, 1, 0, 1, 0, 0],
        'E': [1, 0, 0, 1, 0, 0], 'F': [1, 1, 1, 0, 0, 0], 'G': [1, 1, 1, 1, 0, 0],
        'H': [1, 0, 1, 1, 0, 0], 'I': [0, 1, 1, 0, 0, 0], 'J': [0, 1, 1, 1, 0, 0],
        'K': [1, 0, 0, 0, 1, 0], 'L': [1, 0, 1, 0, 1, 0], 'M': [1, 1, 0, 0, 1, 0],
        'N': [1, 1, 0, 1, 1, 0], 'O': [1, 0, 0, 1, 1, 0], 'P': [1, 1, 1, 0, 1, 0],
        'Q': [1, 1, 1, 1, 1, 0], 'R': [1, 0, 1, 1, 1, 0], 'S': [0, 1, 1, 0, 1, 0],
        'T': [0, 1, 1, 1, 1, 0], 'U': [1, 0, 0, 0, 1, 1], 'V': [1, 0, 1, 0, 1, 1],
        'W': [0, 1, 1, 1, 0, 1], 'X': [1, 1, 0, 0, 1, 1], 'Y': [1, 1, 0, 1, 1, 1],
        'Z': [1, 0, 0, 1, 1, 1], '[': [0, 1, 1, 0, 0, 1], '\\': [1, 0, 1, 1, 0, 1],
        ']': [1, 1, 1, 1, 0, 1], '^': [0, 1, 0, 1, 0, 0], '_': [0, 1, 0, 1, 0, 1]
    }

    total_pages, page_text = Pdf_to_ASCII(path) # pdf에서 아스키값을 읽어옴

    page_text_braille = {} # page_text의 내용을 페이지번호(키)-점자(값)으로 저장할 딕셔너리
    for i in range(total_pages): # 페이지 단위로 점자 변환
        braille_str = [] # 한 페이지의 변환된 점자를 저장하는 곳

        # 아스키값을 점자로 변환하는 과정
        # 아스키값의 입력 값 ex) c c z   e g . o * o b c o i\n\n< 3 c ] j , n +\n\n
        j = 0
        while j < len(page_text[i]):
            if page_text[i][j] == '\n':
                s = page_text[i][j]
                j += 1
            elif page_text[i][j] == ' ':
                s = page_text[i][j]
                j += 2
            else:
                s = braille_ascii_dic[page_text[i][j].upper()]
                j += 2
            braille_str.append(s)
        page_text_braille[i] = braille_str # 페이지번호(키)-점자(값)으로 저장

    return page_text_braille
