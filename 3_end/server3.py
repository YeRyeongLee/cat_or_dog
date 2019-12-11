from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__)

@app.route('/end', methods = ['GET', 'POST'])
def end_again():
   if request.method == 'POST':
      option = request.form['correct']
      if os.path.isfile("./records/record.txt"):
         f = open("./records/record.txt", "a")
      else:
         f = open("./records/record.txt", "w")
      if option == 'yes':
         f.write('1')
         f.close()
         return "Thank you!" + render_template('end.html')
      else:
         f.write('0')
         f.close()
         return "Sorry..." + render_template('end.html')


if __name__ == '__main__':
    #서버 실행
   app.run(debug = True, host='0.0.0.0', port=5003)
