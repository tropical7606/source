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
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        s = str(f)
        f.save('D:/flaskWeb/braille_jy/' + '점자.pdf')


        from braille_to_hangle import brailleRun


        resultText = brailleRun()
        return render_template('/PDF_result.html',fileData = s,testDataHeml = resultText) #결과값 받아오는 코드
        #근데 결과값이 fileUpload페이지로 받아온다. 함수 설정을 그렇게 해서 그런듯


if __name__=='__main__':
    app.run(debug=True)