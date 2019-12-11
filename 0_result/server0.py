from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__)

@app.route('/result')
def render_file():
   if not os.path.isfile("./records/record.txt"):
      return "Logs are not recorded yet"
   f = open("./records/record.txt", "r")
   data = f.read()
   
   total = 0
   correct = 0
   
   for i in data:
      if i == '1':
         correct += 1
      total += 1
   
   if total == 0:
      result = 0
   else:
      result = float(correct) / float(total)
   
   return "The predict result of 'Cat or Dog?' is... \n\t" + str(result) + "%"

if __name__ == '__main__':
    #서버 실행
   app.run(debug = True, host='0.0.0.0', port=9000)
