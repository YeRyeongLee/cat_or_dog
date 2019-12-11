from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

#업로드 HTML 렌더링
@app.route('/upload')
def render_file():
   if request.method == 'POST':
      return render_template('upload.html')
   else:
      return render_template('upload.html')


if __name__ == '__main__':
    #서버 실행
   app.run(debug = True, host='0.0.0.0', port=5001)
