from flask import Flask,request , render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template("main.html")

@app.route('/PDF_trans')
def render_pdf_trans():
    return render_template("PDF_trans.html")

@app.route('/고객센터')
def render_AScenter():
    return render_template("AScenter.html")

@app.route('/PDF_result', methods = ['POST'])
def upload_file():#문제 발생1) 입력값이 3줄 이상부터 번역 불가하다.

    if request.method == 'POST':
        f = request.files.get('file',False)
        language = request.form.get('languageCheck',False)

        s = str(f)
        f.save('D:/flaskWeb/' + '점자.pdf')


        from braille_to_hangle import brailleRun
        from braille_to_eng import EbrailleRun

        #라디오 그룹을 통해 언어 판단
        if (language== "enbr"):  # 점자 -> 영어

            eresultText = EbrailleRun()
            return render_template('/PDF_result.html', fileData=s, testDataHeml=eresultText)  # 결과값 받아오는 코드


        elif(language== "kobr"): #점자->한글

            kresultText = brailleRun()
            kresultText.replace("\n","<br>")
            return render_template('/PDF_result.html',fileData = s,testDataHeml = kresultText) #결과값 받아오는 코드
        elif (language == "ko"):#한글 -> 점자
            #아직 하는 중
            kresultText = brailleRun()

            return render_template('/PDF_result.html', fileData=s, testDataHeml=kresultText)  # 결과값 받아오는 코드
        else: #영어 -> 점자
            # 아직 하는 중
            kresultText = brailleRun()
            return render_template('/PDF_result.html', fileData=s, testDataHeml=kresultText)  # 결과값 받아오는 코드



@app.route('/text_trans')
def render_text_render():
    return render_template("textToB.html")

@app.route('/text_trans', methods = ['POST'])
def render_result_text():
    return render_template("textToB.html")


if __name__=='__main__':
    app.run(host='0.0.0.0', port='5000')