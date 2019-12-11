from flask import Flask, render_template, request
from werkzeug import secure_filename

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

app = Flask(__name__)



FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string("output_graph",
                           "./workspace/animals_graph.pb",
                           "학습된 신경망이 저장된 위치")
tf.app.flags.DEFINE_string("output_labels",
                           "./workspace/animals_labels.txt",
                           "학습할 레이블 데이터 파일")
tf.app.flags.DEFINE_boolean("show_image",
                            False,
                            "이미지 추론 후 이미지를 보여줍니다.")
#이미지 예측 
def predict(imageName):
    labels = [line.rstrip() for line in tf.gfile.GFile(FLAGS.output_labels)]

    with tf.gfile.FastGFile(FLAGS.output_graph, 'rb') as fp:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(fp.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        logits = sess.graph.get_tensor_by_name('final_result:0')
        image = tf.gfile.FastGFile(imageName, 'rb').read()
        prediction = sess.run(logits, {'DecodeJpeg/contents:0': image})

    top_result = int(np.argmax(prediction[0]))
    name = labels[top_result]
    score = prediction[0][top_result]
    return '%s (%.2f%%)' % (name, score * 100)

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      imageName_user = secure_filename(f.filename)
      f.save('./uploads/' + imageName_user)
      predict_result = predict('./uploads/' + imageName_user)
      html_render = render_template('fileUpload.html')
      return predict_result + html_render

if __name__ == '__main__':
    #서버 실행
   app.run(debug = True, host='0.0.0.0', port=5002)
